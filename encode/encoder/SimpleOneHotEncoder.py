from encode.coder.SimpleOneHotCoder import SimpleOneHotCoder


class SimpleOneHotEncoder:
    """
        定义编码规模,对数据进行one-hot编码(0/1编码)
    """

    @staticmethod
    def extend(older: SimpleOneHotCoder, records: list) -> SimpleOneHotCoder:
        """
        对编码器追加特征
        :param older: 旧编码器
        :param records: 所有记录(含说明)
        :return:
        """
        older.descriptions.extend(records)
        code_keys = older.dimensions
        codes = older.codes  # type:set
        for value in records:  # type:dict
            for code_key in code_keys:
                codes.add(code_key + str(value[code_key]))

        return older

    @staticmethod
    def coder(passport: str, records: list, code_keys: set) -> SimpleOneHotCoder:
        """
        通过特征生成一个简单的独热编码器
        :param passport: 通行证(码),用于识别编码问题
        :param records: 编码的所有记录(含说明)
        :param code_keys: 记录中编码的字段名
        :return:
        """
        coder = SimpleOneHotCoder(passport, [], code_keys, set())
        return SimpleOneHotEncoder.extend(coder, records)

    @staticmethod
    def coding(coder: SimpleOneHotCoder, data: list) -> list:
        """
        将数据进行编码效验并返回编码结果
        :param coder:
        :param data:list[dict]
        :return:
        """
        result = []
        codes = coder.codes
        code_keys = coder.dimensions
        for item in data:  # type:dict
            for code_key in code_keys:
                value = code_key + str(item[code_key])
                if value in codes:
                    result.append(value)
                else:
                    raise ValueError("value:%s is not in codes!" % value)

        return result
