from encode.code.ICode import ICode
from encode.combiner.DefaultCombiner import DefaultCombiner


class DimensionCode(ICode):
    """
    一种以维度+值生成唯一码的方法
    """

    @staticmethod
    def code(record: dict, combiner=DefaultCombiner) -> str:
        values = list(record.keys())
        values.extend(record.values())
        return combiner.combine(values)
