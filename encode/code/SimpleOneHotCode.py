class SimpleOneHotCode:
    """
        单个对象的独热编码结果
        1.值可以是具有唯一特性的数值,字符串等
        2.每一行表示一条记录,每一列表示一个维度
        **3.若一条记录存在多个值,则是非法的记录:如位置维度中，若将每一个点看成一个维度特征，则一个物占用多个点是非法的定义
            (实际是维度定义不合理，可以转为用最近的一个点、体积等特征)
    """

    def __init__(self, passport, dimensions: set):
        super().__init__()
        self.passport = passport
        self.code = SimpleOneHotCode(dimensions)
        self.data = []  # type:list
        self.code_data = []  # type:list

    def append(self, data: list, data_dimension):
        """
            添加原始数据,并对其进行OneHot编码
        :param data:
        :param data_dimension:
        :return:
        """
        self.data.append(data)
        for item in data:
            self.code_data.append(item[data_dimension])
