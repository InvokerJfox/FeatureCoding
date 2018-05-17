from encode.code.SimpleOneHotCode import SimpleOneHotCode


class SimpleOneHotEncoder:
    """
        定义数据规模,对数据进行one-hot编码(0/1编码)
    """

    @staticmethod
    def coding(passport, dimensions) -> SimpleOneHotCode:
        """
        通过特征生成一个简单的独热编码器
        :param passport: 通行证(码),用于识别编码问题
        :param dimensions:
        """
        return SimpleOneHotCode(passport, dimensions)

    @staticmethod
    def append(code: SimpleOneHotCode, data: list):
        """
        
        :param code:
        :param data:
        :return:
        """

    def type_check(a, b):
        if a.passport != b.passport:
            raise ValueError("a.passport:%s != b.passport:%s" % a.passport, b.passport)
        if isinstance(a, SimpleOneHotCode) or isinstance(b, SimpleOneHotCode):
            raise ValueError("bit operation function needs <SimpleOneHotCode> but %s and %s found" % type(a), type(b))
        if len(a.record_list) != len(b.record_list):
            raise ValueError(
                "bit operation function needs two same length args,but len:$d and len:%d found" % len(a), len(b))
