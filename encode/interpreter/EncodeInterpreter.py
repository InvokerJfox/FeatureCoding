class EncodeInterpreter:
    """
    编码数据的一般解释器
    """

    def __init__(self, encode_dimensions: list, feature_dimensions=None):
        """

        :param encode_dimensions: 编码维度
        :param feature_dimensions: 保留维度
        """
        super().__init__()
        self.encode_dimensions = encode_dimensions
        if feature_dimensions is None:
            feature_dimensions = []
        self.feature_dimensions = feature_dimensions

    def encodes(self, record: dict) -> dict:
        """
        输出数据的编码维度及其值
        :param record:
        :return:
        """
        r = {}
        for encode in self.encode_dimensions:
            r[encode] = record[encode]
        return r

    def features(self, record: dict) -> dict:
        """
        输出数据的特征维度及其值
        :param record:
        :return:
        """
        r = {}
        for feature in self.feature_dimensions:
            r[feature] = record[feature]
        return r
