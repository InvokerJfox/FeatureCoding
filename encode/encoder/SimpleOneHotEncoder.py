from encode.coder.SimpleOneHotCoder import SimpleOneHotCoder


class SimpleOneHotEncoder:
    """
        定义编码规模,对数据进行one-hot编码(0/1编码)
    """

    @staticmethod
    def register(passport: str, dimensions: list, code_key: str) -> SimpleOneHotCoder:
        """
        通过特征生成一个简单的独热编码器
        :param passport: 通行证(码),用于识别编码问题
        :param dimensions: 编码的所有记录(含说明)
        :param code_key: 记录中编码的字段名
        """
        # 取特征值:多个相同的特征会映射为同一个值
        codes = set()
        for dimension in dimensions:  # type:dict
            codes.add(dimension[code_key])

        return SimpleOneHotCoder(passport, dimensions, codes)

    @staticmethod
    def coding(coder: SimpleOneHotCoder, data: list, code_key: str)->list:
        """
        将数据进行编码效验并返回编码结果
        :param coder:
        :param data:list[dict]
        :param code_key: data中要编码的key
        :return:
        """
        result = []
        codes = coder.codes
        for item in data:  # type:dict
            value = item[code_key]
            if value in codes:
                result.append(value)
            else:
                raise ValueError("value:%s is not in codes!" % value)

        return result
