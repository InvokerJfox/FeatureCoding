import array

from encode.combiner.DefaultCombiner import DefaultCombiner


class DimensionProjector:
    """
    数据按值进行投影
    """

    @staticmethod
    def mapping(records: list, dimensions: list, older: list, combiner=DefaultCombiner) -> list:
        """
        访问每个记录(records),以维度+值(record[dimension])的方式将编码添加至原编码结果(older)中
        并该次数据的编码结果返回
        :param records:
        :param dimensions:
        :param older:
        :param combiner:
        :return:
        """
        newer = []
        for record in records:  # type:dict
            # 唯一码
            mapped = []
            for dimension in dimensions:  # type:str
                # 投影码
                project = combiner.combine([dimension, str(record[dimension])])
                # 判断是否存在
                if project not in older:
                    older.extend([project])
                # 该批次数据的映射结果
                mapped.extend(project)
            # 保存映射结果
            newer.extend(mapped)

        return newer

    @staticmethod
    def match(benchmark, records: list, output: array):
        """
        将数据(records,benchmark同序)基于benchmark进行映射,将结果存储在output中
        output中值为1时表示存在
        :param benchmark:
        :param records:
        :param output:
        :return:
        """
        # 依次对比编码对象,匹配成功则匹配下一个
        benchmark_size = len(benchmark)
        benchmark_index = 0
        for record in records:
            # 编码:
            while benchmark_index < benchmark_size:
                # 若值与编码匹配则标记，且不再查找下一编码
                if record == benchmark[benchmark_index]:
                    output[benchmark_index] = 1
                    break
                benchmark_index += 1

        return output
