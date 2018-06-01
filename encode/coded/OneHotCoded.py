from encode.coder.Coder import Coder
from encode.list.CountingList import CountingList


class OneHotCoded:
    """
    编码器编码结果
    """

    def __init__(self, coder: Coder):
        super().__init__()
        # 数据编码器
        self.coder = coder
        # 编码原数据:{编码后数据的索引:原始数据}
        self.records = CountingList()
        # 数据的唯一编码,及其对应的数据索引
        self.uniques = {}
