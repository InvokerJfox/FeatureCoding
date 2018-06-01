from encode.interpreter.DimensionInterpreter import DimensionInterpreter


class DimensionList:
    """
        具有OneHot唯一编码的列表
    """

    def __init__(self, interpreter=DimensionInterpreter):
        super().__init__()
        # 数据
        self.records = []
        self.interpreter = interpreter

    def extend(self, other: list):
        self.records.extend(other)

    def tolist(self):
        return self.records
