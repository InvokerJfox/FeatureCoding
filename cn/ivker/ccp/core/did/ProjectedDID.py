import numpy as np

from cn.ccp.encode.core.did.CountingDID import CountingList
from cn.ccp.encode.core.projector.OneHotProjector import OneHotProjector


class ProjectedDID(CountingList):
    """
    投影编码结果
    """

    def __init__(self, projector: OneHotProjector):
        """
        初始化一个编码结果存储单元
        """
        super().__init__(projector.interpreter)
        # 编码器
        self.projector = projector
        # 数据的多维编码(函数映射)结果,格式如:[[0,0,1],[1,0,0]]
        self.protected = np.array(())

    def extend(self, records: list) -> list:
        """

        :param records:
        :return: 返回更新索引
        """
        # 获取投影仪
        projector = self.projector
        # 获取已投影数据
        protected = self.protected.tolist()  # type:list

        # 数据(计数)压缩,获取“变化”数据
        update_index = super().extend(records)  # type:list
        update_data = [self.records[uid] for uid in update_index]

        # 对“变化”数据进行重新投影
        update_project = projector.project(update_data)
        # 新增/更新投影
        for pid in range(len(update_project)):
            # 新增
            if len(protected) - 1 < update_index[pid]:
                protected.extend([update_project[pid]])
            # 更新
            else:
                protected[update_index[pid]] = update_project[pid]

        self.protected = np.array(protected)
