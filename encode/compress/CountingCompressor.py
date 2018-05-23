from encode.combiner.DefaultCombiner import DefaultCombiner
from encode.compress.Compressor import Compressor
from encode.identifier.Identifier import Identifier


class CountingCompressor(Compressor):

    @staticmethod
    def compress(records: list, identifier: Identifier, combiner=DefaultCombiner) -> list:
        """
        将原数据(records)按指定维度(encode_dimensions)进行相同值合并,合并时仅保留统计维度(counting_dimensions),并舍弃其他维度
        :param records: list[dict]
        :param identifier:识别器
        :param combiner: 组合器
        :return:
        """
        # 维度识别
        encode_dimensions = identifier.encode_dimensions
        feature_dimensions = identifier.feature_dimensions
        counting_dimensions = identifier.counting_dimensions
        onehot_dimension = identifier.onehot_dimension

        # 取encode_dimensions及其值生成唯一码(dict),将相同值进行映射同时统计维度
        results = {}
        # 遍历所有数据
        for record in records:  # type:dict
            # 取维度&值生成唯一码
            code_list = []
            for encode in encode_dimensions:
                code_list.append(str(encode))
                code_list.append(str(record[encode]))
            code = combiner.combine(code_list)

            # 若存在该记录则更新
            if code not in results:
                value = {}
                # 取编码值
                for encode in encode_dimensions:
                    value[encode] = record[encode]
                # 取特征值
                for feature in feature_dimensions:
                    value[feature] = record[feature]
                # 取统计维度值
                for counting in counting_dimensions:
                    value[counting] = record[counting]
                # 添加onehot唯一码
                value[onehot_dimension] = code  # 用于存储编码唯一码的字段

                results[code] = value
            else:
                value = results[code]
                # 验证特征值
                for feature in feature_dimensions:
                    # 若出现重复特征值则警告
                    if value[feature] != record[feature]:
                        print("WARMING: compressed data's %s has different values: old:%s → new:%s" % (
                            feature, value[feature], record[feature]))

                # 累加统计值
                for counting in counting_dimensions:
                    value[counting] += record[counting]

        return list(results.values())
