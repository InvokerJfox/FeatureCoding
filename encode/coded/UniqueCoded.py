from encode.interpreter.UniqueInterpreter import UniqueInterpreter
from encode.list.UniqueList import UniqueList


class UniqueCoded:
    """
    编码器编码结果
    """

    def __init__(self, interpreter: UniqueInterpreter):
        super().__init__()
        # 编码原数据:{编码后数据的索引:原始数据}
        self.records = UniqueList(interpreter)
        # 数据的唯一编码,及其对应的数据索引
        self.uniques = {}
