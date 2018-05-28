class CountingList:
    """
        基于压缩器对原数据及新数据进行压缩，
        且编码主键具有唯一性；
    """

    def __init__(self):
        super().__init__()
        # 数据
        self.data = []
        #  已存在数据字典表
        self.uniques = set()

    def append(self, other: list):
        CountingList.extend(self, other)

    def extend(self, other: list):
        self.data.extend(other)

    def tolist(self):
        return self.data
