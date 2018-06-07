from encode.encoder.IEncoder import IEncoder
from encode.combiner.DefaultCombiner import DefaultCombiner


class DimensionEncoder(IEncoder):
    """
    一种以维度+值生成唯一码的方法
    """

    @staticmethod
    def encode(record: dict, combiner=DefaultCombiner) -> str:
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
    def hash(record: dict, combiner=DefaultCombiner):
        """
        生成hash码,不强制唯一
        :param record:
        :param combiner:
        :return:
        """
        return hash(DimensionEncoder.encode(record, combiner))
