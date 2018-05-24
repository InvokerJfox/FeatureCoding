from encode.identifier.Identifier import Identifier


class DefaultIdentifier(Identifier):
    def __init__(self, encode_dimensions: list, feature_dimensions=None, counting_dimensions=None):
        """
        数据识别
        :param encode_dimensions: 编码维度:压缩识别
        :param feature_dimensions: 特征维度:压缩后保留的维度,若压缩后存在多个不同值,则提报警告
        :param counting_dimensions: 统计维度:压缩后将该维度进行值累计(累加)
        """
        super().__init__()
        if feature_dimensions is None:
            feature_dimensions = []
        if counting_dimensions is None:
            counting_dimensions = []
        self.encode_dimensions = encode_dimensions
        self.feature_dimensions = feature_dimensions
        self.counting_dimensions = counting_dimensions
