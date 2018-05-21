from encode.coder.MappingOneHotCoder import MappingOneHotCoder


class MappingOneHotEncoder:
    """
        定义编码规模,对数据进行映射型one-hot编码(0/1→0/1编码)
    """

    @staticmethod
    def register(passport: str, dimensions: list, start_key="from", target_key="to") -> MappingOneHotCoder:
        """
        通过特征生成一个映射型独热编码器
        :param passport: 通行证(码),用于识别编码问题
        :param dimensions: 编码的所有记录(含说明)
        :param start_key: 记录中起始态编码的字段名
        :param target_key: 记录中目标态编码的字段名
        """
        # 取特征值:key为start与target的合并，value为start/target分别值
        codes = {}  # type:dict
        for dimension in dimensions:  # type:dict
            start = str(dimension[start_key])
            target = str(dimension[target_key])
            codes.setdefault(start + target, {start_key: start, target_key: target})

        return MappingOneHotCoder(passport, dimensions, codes)

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
            key = start + target
            if codes.get(key) is not None:
                result.setdefault(key, {start_key: start, target_key: target})
            else:
                raise ValueError("key(%s) doesn't in dict(%s)!" % (key, codes))

        return result
