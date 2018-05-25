from encode.interpreter.Interpreter import Interpreter


class MappingInterpreter(Interpreter):
    def __init__(self, start_dimension: str, target_dimension: str, feature_dimensions=None,
                 counting_dimensions=None):
        """
        映射型数据识别器
        :param start_dimension: 起始操作维度
        :param target_dimension: 目标操作维度
        :param feature_dimensions: 特征维度:压缩后保留的维度,若压缩后存在多个不同值,则提报警告
        :param counting_dimensions: 统计维度:压缩后将该维度进行值累计(累加)
        """
        super().__init__()
        if feature_dimensions is None:
            feature_dimensions = []
        if counting_dimensions is None:
            counting_dimensions = []
        self.encode_dimensions = [start_dimension, target_dimension]
        self.start_dimension = start_dimension
        self.target_dimension = target_dimension
        self.feature_dimensions = feature_dimensions
        self.counting_dimensions = counting_dimensions
