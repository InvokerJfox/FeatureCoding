from numpy import zeros

from encode.combiner.DefaultCombiner import DefaultCombiner


class DimensionProjector:
    """
    数据按值进行多维投影
    """

    @staticmethod
    def mapping(records: list, dimensions: list, older: list, combiner=DefaultCombiner):
        """
        访问每个记录(records),以维度+值(record[dimension])的方式将编码添加至原编码结果(older)中
        :param records:
        :param dimensions:
        :param older:
        :param combiner:
        :return:
        """
        for record in records:  # type:dict
            # 所有维度
            for dimension in dimensions:  # type:str
                # 投影码
                project = combiner.combine([dimension, str(record[dimension])])
                # 判断是否存在
                if project not in older:
                    older.extend([project])

    @staticmethod
    def match(records: list, dimensions: list, benchmark: dict, older: list, combiner=DefaultCombiner):
        """
        将数据的维度信息(records+dimensions)基于benchmark进行映射,将结果存储在older中
        并该次数据的编码结果返回
        :param records:
        :param dimensions:
        :param benchmark:
        :param older:二维数组
        :param combiner:
        :return:
        """
        # 依次对比编码对象,匹配成功则匹配下一个
        for record in records:
            # 编码结果
            record_coded = zeros((len(benchmark)))
            # 所有维度
            for dimension in dimensions:
                # 维度映射码
                project = combiner.combine([dimension, str(record[dimension])])
                project_index = benchmark[project]
                # 将该标识码置1
                record_coded[project_index] = 1

            # 新增该记录
            older.extend([record_coded])
