class Coder:
    """
    编码器基础属性
    """

    def __init__(self):
        super().__init__()
        # 数据识别器
        self.compressor = None
        # 编码组合器
        self.combiner = None
        # 原始数据
        self.descriptions = None
        # 唯一编码
        self.codes = None
        # 反向索引
        self.code_indexes = None
