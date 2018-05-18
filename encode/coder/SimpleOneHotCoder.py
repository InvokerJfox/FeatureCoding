class SimpleOneHotCoder:
    """
        单个对象的独热编码表
        1.值可以是具有唯一特性的数值,字符串等
        2.每一行表示一条记录,每一列表示一个维度
        **3.若一条记录存在多个值,则是非法的记录:如位置维度中，若将每一个点看成一个维度特征，则一个物占用多个点是非法的定义
            (实际是维度定义不合理，可以转为用最近的一个点、体积等特征)
    """

    def __init__(self, passport: str, dimensions: list, codes: set):
        """
        初始化一个独热编码表
        :param passport: 通行证
        :param dimensions: 每一个编码对应的说明信息
        :param codes: 用于计算的编码
        """
        super().__init__()
        self.passport = passport
        self.description = dimensions
        self.codes = codes
