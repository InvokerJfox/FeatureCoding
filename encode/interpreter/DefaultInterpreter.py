from encode.interpreter.Interpreter import Interpreter


class DefaultInterpreter(Interpreter):
    """
    描述数据中用于识别的维度
    """

    def __init__(self, encode_dimensions: list):
        super().__init__()
        self.encode_dimensions = encode_dimensions

    def encodes(self, record: dict) -> dict:
        """
        输出数据的编码维度及其值
        :param record:
        :return:
        """
        r = {}
        for encode in self.encode_dimensions:
            r[encode] = record[encode]
        return r
