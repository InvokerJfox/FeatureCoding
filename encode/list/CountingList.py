from encode.code.DimensionCode import DimensionCode
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.list.UniqueList import UniqueList


class CountingList(UniqueList):
    def __init__(self, interpreter: CountingInterpreter):
        """

        :param interpreter:
        """
        super().__init__(interpreter)

    def extend(self, records: list):
        """
        新增数据,按指定维度(encode_dimensions)进行相同值合并,合并时仅保留统计维度(counting_dimensions),并舍弃其他维度
        :param records:
        :return:
        """

        # 读取数据和解释器
        interpreter = self.interpreter
        older = self.records

        # 读取唯一码出现的list索引,记录新数据反射记录索引
        uniques = self.uniques
        unique_index = len(uniques)

        # 遍历所有数据
        for record in records:  # type:dict
            # 取维度值
            encodes = interpreter.encodes(record)  # type:dict
            features = interpreter.features(record)  # type:dict
            counting = interpreter.counting(record)  # type:dict

            # 取唯一码，不存在时用组合器生成
            unique = interpreter.unique(record)
            if unique is None:
                unique = DimensionCode.code(encodes)

            # 若不存在该记录则更新
            if unique not in uniques:
                # 新建该记录
                value = {interpreter.unique_dimension: unique}
                # 取编码值 & 特征值 & 统计维度值
                value.update(encodes)
                value.update(features)
                value.update(counting)

                # 添加至结果 & 记录索引
                older.extend([value])
                uniques[unique] = unique_index

                # 索引自增
                unique_index += 1
            else:
                # 存在则验合特征值并累加统计值
                value = older[uniques[unique]]
                # 验证特征值
                feature_dimensions = interpreter.feature_dimensions
                for feature in feature_dimensions:
                    # 若出现重复特征值则警告
                    if value[feature] != record[feature]:
                        print("WARMING: CountingCompressor compressed dimension:[%s]"
                              " two different values: old:[%s] → new:[%s]" % (feature, value[feature], record[feature]))

                # 累加统计值
                counting = interpreter.counting_dimension
                value[counting] += record[counting]
