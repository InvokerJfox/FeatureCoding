from cn.ivker.encode.core.did.EncodeDID import EncodeFID
from cn.ivker.encode.core.encoder.DimensionEncoder import DimensionEncoder
from cn.ivker.encode.core.interpreter.UniqueInterpreter import UniqueInterpreter


class UniqueDID(EncodeDID):
    def __init__(self, interpreter: UniqueInterpreter):
        super().__init__(interpreter)
        #  数据字典表,及其对应的数据索引
        self.uniques = {}

    def extend(self, records: list) -> list:
        """
        新增数据,按指定维度(encode_dimensions)生成唯一码并进行相同值合并
        :param records:
        :return:返回更新索引
        """

        # 读取数据和解释器
        interpreter = self.interpreter
        older = self.records

        # 读取唯一码出现的list索引,记录新数据反射记录索引
        uniques = self.uniques
        record_index = len(uniques)

        # 记录更新的记录所有并返回
        update_indexes = {}

        # 遍历所有数据
        for record in records:  # type:dict
            # 取维度值
            encodes = interpreter.encodes(record)  # type:dict
            features = interpreter.features(record)  # type:dict

            # 取唯一码，不存在时用组合器生成
            unique = interpreter.unique(record)
            if unique is None:
                unique = DimensionEncoder.encode(encodes)

            # 若不存在该记录则更新
            if unique not in uniques:
                # 新建该记录
                value = {interpreter.unique_dimension: unique}
                # 取编码值 & 特征值 & 统计维度值
                value.update(encodes)
                value.update(features)

                # 添加至结果 & 记录索引
                older.extend([value])
                uniques[unique] = record_index

                # 索引自增
                record_index += 1
            else:
                # 出现重复唯一码,提示
                print("WARMING: UniqueList got duplicate unique id[%s],Ignored" % unique)

            # 记录更新记录
            update_indexes.setdefault(uniques[unique])

        return list(update_indexes.keys())
