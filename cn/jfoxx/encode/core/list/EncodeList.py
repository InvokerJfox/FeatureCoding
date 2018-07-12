from encode.interpreter.EncodeInterpreter import EncodeInterpreter

from cn.jfoxx.encode.core.list.List import List


class EncodeList(List):
    """
        具有OneHot唯一编码的列表
    """

    def __init__(self, interpreter: EncodeInterpreter):
        """
        初始化
        :param interpreter:
        """

        super().__init__(interpreter)

    def extend(self, records: list):
        """
        新增数据
        :param records:
        :return:返回更新索引
        """
        super().extend(records)
