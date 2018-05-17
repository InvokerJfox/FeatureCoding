class SimpleMapCoder:
    """
    映射编码结果
    1.映射的起始和目标态值可以是具有唯一特性的数值,字符串等
    2.若一条记录的起始和目标态存在多个值,则是非法的记录:如起始操作未知品质，会获得合格品质或不合格品质是非法的
    """

    def __init__(self, passport, dimensions: dict):
        super().__init__()
        self.passport = passport
        self.record_list = dimensions
