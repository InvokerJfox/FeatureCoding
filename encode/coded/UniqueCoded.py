from encode.interpreter.UniqueInterpreter import UniqueInterpreter
from encode.list.UniqueList import UniqueList


class UniqueCoded:
    """
    编码器编码结果
    """

    def __init__(self, interpreter: UniqueInterpreter):
        """
        初始化编码原始数据
        :param interpreter: 维度解释器
        """
        super().__init__()
        # 编码原数据,具有唯一主键
        self.records = UniqueList(interpreter)
