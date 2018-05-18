class MappingOneHotCoder:
    """
    映射编码表
    1.映射的起始和目标态值可以是具有唯一特性的数值,字符串等
    2.若一条记录的起始和目标态存在多个值,则是非法的记录:如起始操作未知品质，会获得合格品质或不合格品质是非法的
    """

    def __init__(self, passport: str, dimensions: list, codes: dict):
        """
        初始化一个映射编码表
        :param passport: 通行证
        :param dimensions: 每一个编码对应的说明信息
        :param codes: 用于计算的编码的key为start与target的合并，value为start/target分别值
        """
        super().__init__()
        self.passport = passport
        self.description = dimensions
        self.codes = codes
