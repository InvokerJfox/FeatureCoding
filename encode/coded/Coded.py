from encode.coder.Coder import Coder
from encode.list.CountingList import CountingList


class Coded:
    """
    编码器基础属性
    """

    def __init__(self, coder: Coder):
        super().__init__()
        # 数据编码器
        self.coder = coder
        # 编码原数据:{编码后数据的索引:原始数据}
        self.descriptions = CountingList(coder.compressor)
        # 数据的唯一编码
        self.coded = []
        # 数据唯一编码的反向索引
        self.coded_indexes = {}
