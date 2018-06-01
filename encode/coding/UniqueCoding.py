from encode.interpreter import UniqueInterpreter
from encode.list.UniqueList import UniqueList


class UniqueCoding:
    """
    编码器的译码
    """

    def __init__(self, interpreter: UniqueInterpreter):
        """
        初始化编码原始数据
        :param interpreter:
        """
        super().__init__()
        # 原始数据,具有唯一主键
        self.records = UniqueList(interpreter)
