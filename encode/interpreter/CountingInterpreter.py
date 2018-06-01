from encode.interpreter.UniqueInterpreter import UniqueInterpreter


class CountingInterpreter(UniqueInterpreter):
    def __init__(self, encode_dimensions: list, feature_dimensions=None, counting_dimension=None):
        """
        数据识别
        :param encode_dimensions: 编码维度:压缩识别
        :param feature_dimensions: 特征维度:压缩后保留的维度,若压缩后存在多个不同值,则提报警告
        :param counting_dimension: 统计维度:压缩后将该维度进行值累计(累加)
        """
        super().__init__(encode_dimensions, feature_dimensions)
        if counting_dimension is None:
            counting_dimension = []
        self.counting_dimension = counting_dimension

    def counting(self, record: dict) -> dict:
        """
        输出数据的计数维度及其值
        :param record:
        :return:
        """
        counting = self.counting_dimension
        return {counting: record[counting]}
