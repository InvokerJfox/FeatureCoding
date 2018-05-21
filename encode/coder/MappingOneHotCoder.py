class MappingOneHotCoder:
    """
    映射编码表
    1.映射的起始和目标态值可以是具有唯一特性的数值,字符串等
    2.若一条记录的起始和目标态存在多个值,则是非法的记录:如起始操作未知品质，会获得合格品质或不合格品质是非法的
    """

    def __init__(self, passport: str, records: list, start_key: str, target_key: str, codes: dict):
        """
        初始化一个映射编码表
        :param passport: 通行证
        :param records: 编码前原始信息
        :param start_key: 进行编码的起始维度
        :param target_key: 进行编码的目标维度
        :param codes: 编码结果,字典类型;key为start与target的合并，value为start/target分别值
        """
        super().__init__()
        self.passport = passport
        self.descriptions = records
        self.start_key = start_key
        self.target_key = target_key
        self.codes = codes
