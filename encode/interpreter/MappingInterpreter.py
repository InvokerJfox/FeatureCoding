from encode.interpreter.CountingInterpreter import CountingInterpreter


class MappingInterpreter(CountingInterpreter):
    def __init__(self, start_dimension: str, target_dimension: str, encode_dimensions: list,
                 state_default=None, feature_dimensions=None, counting_dimensions=None):

        """
        映射型数据识别器
        :param start_dimension: 起始操作维度
        :param target_dimension: 目标操作维度
        :param encode_dimensions: 起始&目标操作维度中编码维度
        :param state_default:当编码后状态维度为空时,填入该默认值
        :param feature_dimensions: 特征维度:压缩后保留的维度,若压缩后存在多个不同值,则提报警告
        :param counting_dimensions: 统计维度:压缩后将该维度进行值累计(累加)
        """

        if state_default is None:
            state_default = {}
        if feature_dimensions is None:
            feature_dimensions = []
        if counting_dimensions is None:
            counting_dimensions = []
        self.start_dimension = start_dimension
        self.target_dimension = target_dimension
        self.encode_dimensions = encode_dimensions
        self.state_default = state_default
        self.feature_dimensions = feature_dimensions
        self.counting_dimensions = counting_dimensions
        super().__init__(encode_dimensions, feature_dimensions, counting_dimensions)
