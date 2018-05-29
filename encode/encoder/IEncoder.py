from encode.coded.Coded import Coded
from encode.coder.Coder import Coder


class IEncoder:
    def coding(self, records: list) -> Coder:
        pass

    def encoding(self, records: list) -> Coded:
        pass
