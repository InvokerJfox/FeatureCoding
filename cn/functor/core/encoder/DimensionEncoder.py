from encode.utility.string.StringCombiner import StringCombiner

from cn.functor.encode.encoder import IEncoder


class DimensionEncoder(IEncoder):
    """
    一种以维度+值生成唯一码的方法
    """

    @staticmethod
    def encode(record: dict, combiner=StringCombiner) -> str:
        """
        生成维度组合码
        :param record:
        :param combiner:
        :return:
        """
        values = list(record.keys())
        values.extend(record.values())
        return combiner.combine(values)

    @staticmethod
    def hash(record: dict, combiner=StringCombiner):
        """
        生成hash码,不强制唯一
        :param record:
        :param combiner:
        :return:
        """
        return hash(DimensionEncoder.encode(record, combiner))
