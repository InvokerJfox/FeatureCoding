from encode.interpreter.EncodeInterpreter import EncodeInterpreter


class UniqueInterpreter(EncodeInterpreter):
    """
    具有唯一编码的数据解释器
    """

    def __init__(self, encode_dimensions: list, hold_dimensions=None):
        super().__init__(encode_dimensions, hold_dimensions)
        # 用于存储编码唯一码的字段
        self.unique_dimension = "onehotid"

    def unique(self, record: dict) -> str:
        """
        返回unique值
        :param record:
        :return:
        """
        return record.get(self.unique_dimension)
