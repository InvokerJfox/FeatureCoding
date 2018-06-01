from encode.coded.UniqueCoded import UniqueCoded
from encode.coding.UniqueCoding import UniqueCoding
from encode.list.UniqueList import UniqueList


class IEncoder:
    """
    增量式编码器接口
    """

    @staticmethod
    def learn(coding: UniqueCoding, records: UniqueList):
        pass

    @staticmethod
    def forget(coding: UniqueCoding, indexes: list):
        pass

    @staticmethod
    def encode(coded: UniqueCoded, coding: UniqueCoding, records: UniqueList):
        pass

    @staticmethod
    def decode(coded: UniqueCoded, indexes: list):
        pass
