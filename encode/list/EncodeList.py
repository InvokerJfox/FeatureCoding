from encode.interpreter.EncodeInterpreter import EncodeInterpreter


class EncodeList:
    """
        具有OneHot唯一编码的列表
    """

    def __init__(self, interpreter: EncodeInterpreter):
        super().__init__()
        # 数据
        self.records = []
        self.interpreter = interpreter

    def tolist(self):
        return self.records
