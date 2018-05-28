from encode.coded.Coded import Coded
from encode.coder.Coder import Coder


class IEncoder:
    def coder(self, records: list) -> Coder:
        pass

    def coding(self, records: list) -> Coded:
        pass
