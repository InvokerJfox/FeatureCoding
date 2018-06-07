from numpy import zeros

from encode.encoder.DimensionEncoder import DimensionEncoder
from encode.interpreter.Interpreter import Interpreter
from encode.learner.ILearner import ILearner


class OneHotProjector(ILearner):
    """
    数据按 维度+值 进行多维投影
    """

    def __init__(self, interpreter: Interpreter):
        super().__init__()
        self.interpreter = interpreter
        # 投影结果及投影对应的投影索引
        self.projects = {}
        # 投影结果对应的数据索引(多个)
        self.project_indexes = {}

    def feed(self, records: list):
        """
        访问每个记录(records),以维度+值(record[dimension])的方式将编码添加至原编码结果(projects)中
        :param records:
        :return:
        """
        # 投影维度
        dimensions = self.interpreter.dimensions
        # 投影值
        projects = self.projects
        # 全量数据索引
        project_indexes = self.project_indexes
        project_index = len(self.records)
        # 添加历史记录
        self.records.extend(records)

        for record in records:  # type:dict
            # 所有维度
            for dimension in dimensions:  # type:str
                # 投影码
                project = DimensionEncoder.encode({dimension: str(record[dimension])})
                # 若投影不存在则添加
                if project not in projects:
                    projects[project] = len(projects)
                # 记录投影对应的数据id
                project_indexes.setdefault(project, [])
                project_indexes[project].extend([project_index])
                project_index += 1

    def leak(self, indexes: list):
        pass

    def project(self, records: list) -> list:
        """
        将数据的维度信息(records+dimensions)基于projects进行映射,将结果存储在projects中
        并该次数据的编码结果返回
        :param records:
        :return:
        """
        #
        projected = []
        # 投影维度
        dimensions = self.interpreter.dimensions
        # 投影值
        projects = self.projects
        # 依次对比编码对象,匹配成功则匹配下一个
        for record in records:
            # 编码结果
            record_coded = zeros((len(projects)), dtype=int)
            # 所有维度
            for dimension in dimensions:
                # 维度映射码
                project = DimensionEncoder.encode({dimension: str(record[dimension])})
                project_index = projects[project]
                # 将该标识码置1
                record_coded[project_index] = 1

            # 新增该记录
            projected.extend([record_coded.tolist()])

        return projected
