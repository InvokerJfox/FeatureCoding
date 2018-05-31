from encode.code.DimensionCode import DimensionCode
from encode.compressor.ICompressor import ICompressor
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.list.CountingList import CountingList


class CountingCompressor(ICompressor):
    def __init__(self, interpreter: CountingInterpreter):
        """
        :param interpreter:解释器
        """
        super().__init__()
        self.interpreter = interpreter

    def compress(self, records: list) -> CountingList:
        """
        将原数据(records)按指定维度(encode_dimensions)进行相同值合并,合并时仅保留统计维度(counting_dimensions),并舍弃其他维度
        :param records: list[dict]
        :return:计数列表
        """

        # 计数列表
        cl = CountingList()
        recs = []

        # 解释器
        interpreter = self.interpreter  # type :CountingInterpreter

        # 记录第一次唯一码出现的list索引
        uniques = dict()
        # 遍历所有数据
        record_index = 0
        for record in records:  # type:dict
            # 取维度值
            encodes = interpreter.encodes(record)  # type:dict
            features = interpreter.features(record)  # type:dict
            counting = interpreter.counting(record)  # type:dict

            # 取唯一码，不存在时用组合器生成
            onehot = interpreter.onehot(record)
            if onehot is None:
                onehot = DimensionCode.code(encodes)

            # 若不存在该记录则更新
            if onehot not in uniques:
                # 新建该记录
                value = {interpreter.onehot_dimension: onehot}
                # 取编码值 & 特征值 & 统计维度值
                value.update(encodes)
                value.update(features)
                value.update(counting)

                # 添加至结果 & 记录索引
                recs.extend([value])
                uniques[onehot] = record_index
            else:
                # 存在则验合特征值并累加统计值
                value = recs[uniques[onehot]]
                # 验证特征值
                feature_dimensions = interpreter.feature_dimensions
                for feature in feature_dimensions:
                    # 若出现重复特征值则警告
                    if value[feature] != record[feature]:
                        print("WARMING: compressed coded's %s has different values: old:%s → new:%s" % (
                            feature, value[feature], record[feature]))

                # 累加统计值
                counting = interpreter.counting_dimension
                value[counting] += record[counting]

                # 索引自增
                record_index += 1

        # 存储数据
        cl.records = recs
        # 将数据提取出唯一码,并生成对应数据的索引
        uni = list(map(lambda rec: interpreter.onehot(rec), recs))
        cl.uniques = dict(zip(uni, range(len(uni))))

        return cl
