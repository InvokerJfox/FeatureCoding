from numpy import zeros

from encode.combiner.DefaultCombiner import DefaultCombiner
from encode.projector.IProjector import IProjector


class DimensionProjector(IProjector):
    """
    数据按值进行多维投影
    """

    @staticmethod
    def project(records: list, dimensions: list, projects: dict, combiner=DefaultCombiner):
        """
        访问每个记录(records),以维度+值(record[dimension])的方式将编码添加至原编码结果(projects)中
        :param records:
        :param dimensions:
        :param projects:
        :param combiner:
        :return:
        """
        for record in records:  # type:dict
            # 所有维度
            for dimension in dimensions:  # type:str
                # 投影码
                project = combiner.combine([dimension, str(record[dimension])])
                # 判断是否存在
                if project not in projects:
                    projects[project] = len(projects)

    @staticmethod
    def projecting(records: list, dimensions: list, projects: dict, projected: list, combiner=DefaultCombiner):
        """
        将数据的维度信息(records+dimensions)基于projects进行映射,将结果存储在projects中
        并该次数据的编码结果返回
        :param records:
        :param dimensions:
        :param projects:
        :param projected:二维数组
        :param combiner:
        :return:
        """
        # 依次对比编码对象,匹配成功则匹配下一个
        for record in records:
            # 编码结果
            record_coded = zeros((len(projects)))
            # 所有维度
            for dimension in dimensions:
                # 维度映射码
                project = combiner.combine([dimension, str(record[dimension])])
                project_index = projects[project]
                # 将该标识码置1
                record_coded[project_index] = 1

            # 新增该记录
            projected.extend([record_coded])
