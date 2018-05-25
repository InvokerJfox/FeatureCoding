from encode.combiner.DefaultCombiner import DefaultCombiner
from encode.interpreter.Interpreter import Interpreter


class Compressor:
    def __init__(self, interpreter: Interpreter, combiner=DefaultCombiner):
        super().__init__()
        self.interpreter = interpreter
        self.combiner = combiner

    def compress(self, records: list) -> list:
        """
        对数据进行压缩
        :param records:
        :return:
        """
        pass
