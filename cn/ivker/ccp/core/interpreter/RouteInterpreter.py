from cn.ivker.ccp.core.interpreter.UniqueInterpreter import UniqueInterpreter


class MappingInterpreter(UniqueInterpreter):
    def __init__(self, start_dimension: str, target_dimension: str, encode_dimensions: list, feature_dimensions=None):
        """
        映射型数据识别器
        :param start_dimension: 起始操作维度
        :param target_dimension: 目标操作维度
        :param encode_dimensions: 起始&目标操作维度中编码维度
        :param feature_dimensions: 特征维度:压缩后保留的维度,若压缩后存在多个不同值,则提报警告
        """
        self.start_dimension = start_dimension
        self.target_dimension = target_dimension
        super().__init__(encode_dimensions, feature_dimensions)

    def starts(self, record: dict) -> dict:
        """
        输出数据的计数维度及其值
        :param record:
        :return:
        """
        return record[self.start_dimension]

    def targets(self, record: dict) -> dict:
        """
        输出数据的计数维度及其值
        :param record:
        :return:
        """
        return record[self.target_dimension]
