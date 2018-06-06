import numpy as np

from encode.encoded.Encoded import Encoded
from encode.interpreter.EncodeInterpreter import EncodeInterpreter
from encode.list.EncodeList import EncodeList
from encode.projector.OneHotProjector import OneHotProjector


class ProjectEncoded(Encoded):
    """
    投影编码结果
    """

    def __init__(self, projector: OneHotProjector):
        """
        初始化一个编码结果存储单元
        """
        super().__init__()
        # 编码器
        self.projector = projector
        # 数据
        self.records = []
        # 数据的多维编码(函数映射)结果,格式如:[[0,0,1],[1,0,0]]
        self.protected = np.array(())

    def extend(self, records: list):
        # 获取投影仪
        projector = self.projector
        # 获取已投影数据
        protected = self.protected.tolist()  # type:list

        # 记录数据
        self.records.extend(records)
        # 记录投影
        protected.extend(projector.project(records))
        self.protected = np.array(protected)

    def remove(self, indexes: list):
        pass
