from encode.compressor.CountingCompressor import CountingCompressor
from encode.list.CountingList import CountingList


class Coder:
    """
    编码器基础属性
    """

    def __init__(self, compressor: CountingCompressor):
        super().__init__()
        # 数据识别器
        self.compressor = compressor
        # 原始数据
        self.records = CountingList(compressor)
        # 唯一编码
        self.uniques = []
        # 反向索引,唯一编码对应记录的索引
        self.unique_indexes = {}
