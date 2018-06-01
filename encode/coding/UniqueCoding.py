from encode.list.UniqueList import UniqueList


class UniqueCoding:
    """
    编码器的译码
    """

    def __init__(self):
        super().__init__()
        # 原始数据
        self.records = UniqueList()
        # 唯一编码,及其对应记录的索引
        self.uniques = {}
