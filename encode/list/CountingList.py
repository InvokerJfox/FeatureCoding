from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.list.UniqueList import UniqueList


class CountingList(UniqueList):
    def __init__(self, interpreter: CountingInterpreter):
        super().__init__(interpreter)
