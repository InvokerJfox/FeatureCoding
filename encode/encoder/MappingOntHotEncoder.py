from encode.coder.MappingOneHotCoder import MappingOneHotCoder


class MappingOneHotEncoder:
    """
        定义编码规模,对数据进行映射型one-hot编码(0/1→0/1编码)
    """

    @staticmethod
    def expand(older: MappingOneHotCoder, records: list) -> MappingOneHotCoder:
        """
        对编码器追加特征
        :param older: 旧编码器
        :param records: 所有记录(含说明)
        """
        # 取特征值:key为start与target的合并，value为start/target分别值
        codes = older.codes  # type:dict
        start_key = older.start_key
        target_key = older.target_key
        for value in records:  # type:dict
            start = str(value[start_key])
            target = str(value[target_key])
            codes.setdefault(start_key + start + target_key + target, {start_key: start, target_key: target})
        older.descriptions.append(records)

        return older

    @staticmethod
    def coder(passport: str, records: list, start_key="from", target_key="to") -> MappingOneHotCoder:
        """
        通过特征生成一个映射型独热编码器
        :param passport: 通行证(码),用于识别编码问题
        :param records: 编码的所有记录(含说明)
        :param start_key: 记录中起始态编码的字段名
        :param target_key: 记录中目标态编码的字段名
        :return:
        """
        coder = MappingOneHotCoder(passport, [], start_key, target_key, {})
        return MappingOneHotEncoder.expand(coder, records)

    @staticmethod
    def coding(coder: MappingOneHotCoder, data: list, start_key="from", target_key="to") -> list:
        """
        将数据进行编码效验并返回编码结果
        :param coder:
        :param data:list[dict]
        :param start_key:
        :param target_key:
        :return:
        """
        result = {}
        codes = coder.codes
        for item in data:  # type:dict
            start = str(item[start_key])
            target = str(item[target_key])
            key = start_key + start + target_key + target
            if codes.get(key) is not None:
                result.setdefault(key, {start_key: start, target_key: target})
            else:
                raise ValueError("key(%s) doesn't in dict(%s)!" % (key, codes))

        return result
