from numpy import array

from encode.encoded.Encoded import Encoded
from encode.list.UniqueList import UniqueList


class ProjectEncoded(Encoded):
    """
    投影编码结果
    """

    def __init__(self, records: UniqueList):
        """
        初始化一个编码结果存储单元
        :param records:
        """
        super().__init__(records)
        # 数据的多维编码(函数映射)结果,格式如:[[0,0,1],[1,0,0]]
        self.protected = array(())

    def decode(self, coded: list, indexes: list) -> list:
        super().decode(coded, indexes)

    def encode(self, decoding: list, records: list) -> list:
        return super().encode(decoding, records)
