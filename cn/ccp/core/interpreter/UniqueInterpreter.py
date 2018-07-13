from cn.ccp.encode.core.interpreter.EncodeInterpreter import EncodeInterpreter


class UniqueInterpreter(EncodeInterpreter):
    """
    具有唯一编码的数据解释器
    """

    def __init__(self, dimensions: list, encode_dimensions: list, feature_dimensions=None):
        super().__init__(dimensions, encode_dimensions, feature_dimensions)
        # 用于存储编码唯一码的字段
        self.unique_dimension = "onehotid"

    def unique(self, record: dict) -> str:
        """
        返回unique值
        :param record:
        :return:
        """
        return record.get(self.unique_dimension)
