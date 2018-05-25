class Interpreter:
    """
    解释数据维度的识别信息
    """

    def __init__(self):
        super().__init__()
        self.encode_dimensions = []
        self.onehot_dimension = "onehotid"  # 用于存储编码唯一码的字段

    def onehot(self, record: dict):
        """
        返回onehot值
        :param record:
        :return:
        """
        return record.get(self.onehot_dimension)
