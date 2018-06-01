from encode.interpreter.EncodeInterpreter import EncodeInterpreter


class EncodeList:
    """
        具有OneHot唯一编码的列表
    """

    def __init__(self, interpreter: EncodeInterpreter, records=None):
        """

        :param interpreter:
        :param records:
        """
        if records is None:
            records = []

        super().__init__()
        # 数据
        self.records = records
        self.interpreter = interpreter
