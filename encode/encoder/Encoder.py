from encode.coded.Coded import Coded
from encode.coder.Coder import Coder
from encode.list.CountingList import CountingList


class Encoder:
    @staticmethod
    def coder(records: CountingList, identifier=None, coder=None) -> Coder:
        pass

    @staticmethod
    def coding(records: CountingList, coder: Coder, coded=None) -> Coded:
        pass
