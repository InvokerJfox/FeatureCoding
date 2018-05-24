from encode.compressor.CountingCompressor import CountingCompressor
from encode.identifier.Identifier import Identifier


class UniqueList(list):
    """
    具有唯一性的数据，具有唯一的编码字段
    """

    def __init__(self, identifier: Identifier):
        super().__init__()
        self.identifier = identifier

    def append(self, other: list):
        UniqueList.extend(self, other)

    def extend(self, other: list):
        super().extend(CountingCompressor.compress(other, self.identifier))

    def increment(self, other: list) -> list:
        """
        自身并上该集合，并返回增量集合
        :param other:
        :return:
        """
        inc = list(set(other) - set(self))
        super().extend(inc)
        return inc
