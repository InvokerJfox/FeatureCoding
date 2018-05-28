from encode.combiner.DefaultCombiner import DefaultCombiner
from encode.compressor.Compressor import Compressor
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.list.CountingList import CountingList


class CountingCompressor(Compressor):
    def __init__(self, interpreter: CountingInterpreter, combiner=DefaultCombiner):
        """
        :param interpreter:解释器
        :param combiner: 组合器
        """
        super().__init__(interpreter, combiner)

    def compress(self, records: list) -> CountingList:
        """
        将原数据(records)按指定维度(encode_dimensions)进行相同值合并,合并时仅保留统计维度(counting_dimensions),并舍弃其他维度
        :param records: list[dict]
        :return:计数列表
        """

        # 计数列表
        cl = CountingList()

        # 解释器
        interpreter = self.interpreter  # type :CountingInterpreter

        # 取encode_dimensions及其值生成唯一码(dict),将相同值进行映射同时统计维度
        uniques = {}
        # 遍历所有数据
        for record in records:  # type:dict
            # 取维度值
            encodes = interpreter.encodes(record)  # type:dict
            features = interpreter.features(record)  # type:dict
            counting = interpreter.countings(record)  # type:dict

            # 取唯一码，不存在时用组合器生成
            onehot = interpreter.onehot(record)
            if onehot is None:
                values = list(encodes.keys())
                values.extend(encodes.values())
                onehot = self.combiner.combine(values)

            # 若不存在该记录则更新
            if onehot not in uniques:
                # 新建该记录
                value = {interpreter.onehot_dimension: onehot}
                # 取编码值 & 特征值 & 统计维度值
                value.update(encodes)
                value.update(features)
                value.update(counting)

                # 添加至结果
                uniques[onehot] = value
            else:
                # 存在则验合特征值并累加统计值
                value = uniques[onehot]
                # 验证特征值
                feature_dimensions = interpreter.feature_dimensions
                for feature in feature_dimensions:
                    # 若出现重复特征值则警告
                    if value[feature] != record[feature]:
                        print("WARMING: compressed coded's %s has different values: old:%s → new:%s" % (
                            feature, value[feature], record[feature]))

                # 累加统计值
                counting_dimensions = interpreter.counting_dimensions
                for counting in counting_dimensions:
                    value[counting] += record[counting]

        # 唯一码字典
        cl.data = list(uniques.values())
        cl.uniques = set(uniques.keys())

        return cl
