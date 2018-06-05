from numpy import zeros

from encode.code.DimensionCode import DimensionCode
from encode.decoding.IDecoding import IDecoding
from encode.interpreter.DefaultInterpreter import DefaultInterpreter
from encode.projector.IProjector import IProjector


class OneHotProjector(IDecoding, IProjector):
    """
    数据按 维度+值 进行多维投影
    """

    def __init__(self, interpreter: DefaultInterpreter):
        super().__init__()
        self.interpreter = interpreter
        self.projects = {}

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

        for record in records:  # type:dict
            # 所有维度
            for dimension in dimensions:  # type:str
                # 投影码
                project = DimensionCode.code({dimension: str(record[dimension])})
                # 判断是否存在
                if project not in projects:
                    projects[project] = len(projects)

    def project(self, records: list):
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
            record_coded = zeros((len(projects)),dtype=int)
            # 所有维度
            for dimension in dimensions:
                # 维度映射码
                project = DimensionCode.code({dimension: str(record[dimension])})
                project_index = projects[project]
                # 将该标识码置1
                record_coded[project_index] = 1

            # 新增该记录
            projected.extend([record_coded.tolist()])

        return projected
