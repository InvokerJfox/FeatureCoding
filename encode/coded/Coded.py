class Coded:
    """
    编码器基础属性
    """

    def __init__(self):
        super().__init__()
        # 数据识别器
        self.coder = None
        # 原始数据
        self.descriptions = None
        # 唯一编码
        self.coded = None
        # 反向索引
        self.coded_indexes = None
