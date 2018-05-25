from encode.compressor.CountingCompressor import CountingCompressor


class CountingList:
    """
        基于压缩器对原数据及新数据进行压缩，
        且编码主键具有唯一性；
    """

    def __init__(self, compressor: CountingCompressor):
        super().__init__()
        # 数据
        self.data = []
        #  已存在数据字典表
        self.uniques = set()
        # 压缩器
        self.compressor = compressor

    def append(self, other):
        CountingList.extend(self, other)

    def extend(self, other: list):
        """
        添加数据,将会对输入的数据进行压缩处理
        :param other:
        :return:
        """
        # 压缩器和唯一码主键
        compressor = self.compressor
        onehot = self.compressor.interpreter.onehot_dimension

        # 累积新旧数据，进行压缩
        cum = self.data
        cum.extend(other)
        self.data = compressor.compress(cum)

        # 唯一码字典
        self.uniques = set(map(lambda x: x[onehot], self.data))

    def increment(self, other: list) -> list:
        """
        集合并上新集合，并返回其中的编码上的编码增量(encode value)集合
        :param other:
        :return:
        """
        compressor = self.compressor
        onehot = self.compressor.interpreter.onehot_dimension
        # 对新数据进行压缩
        newed = compressor.compress(other)

        # 唯一码字典
        uniques = self.uniques
        # 计算增量
        inc = []
        for record in newed:
            code = record[onehot]
            # 不存在则添加数据，保存为增量
            if code not in uniques:
                uniques.add(record)
                inc.extend(record)

        # 存储新数据
        self.extend(other)

        # 返回编码增量
        return inc

    def tolist(self):
        return self.data
