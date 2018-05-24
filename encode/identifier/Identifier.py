class Identifier:
    """
    用于数据预处理中,数据维度的识别信息
    """

    def __init__(self):
        super().__init__()
        self.encode_dimensions = []
        self.feature_dimensions = []
        self.counting_dimensions = []
        self.onehot_dimension = "onehotid"  # 用于存储编码唯一码的字段
