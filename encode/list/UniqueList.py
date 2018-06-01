from encode.interpreter.UniqueInterpreter import UniqueInterpreter
from encode.list.EncodeList import EncodeList


class UniqueList(EncodeList):
    def __init__(self, interpreter: UniqueInterpreter):
        super().__init__(interpreter)
        #  已存在数据字典表,及其对应的数据索引
        self.uniques = {}
