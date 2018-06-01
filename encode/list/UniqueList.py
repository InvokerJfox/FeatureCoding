from encode.interpreter.DimensionInterpreter import DimensionInterpreter
from encode.list.DimensionList import DimensionList


class UniqueList(DimensionList):
    def __init__(self, interpreter=DimensionInterpreter):
        super().__init__(interpreter)
        #  已存在数据字典表,及其对应的数据索引
        self.uniques = {}

    def extend(self, other: list):
        self.records.extend(other)
        # 将数据提取出唯一码,并生成对应数据的索引
        interpreter = self.interpreter
        uni = list(map(lambda rec: interpreter.onehot(rec), other))
        self.uniques = dict(zip(uni, range(len(uni))))
