from encode.interpreter.EncodeInterpreter import EncodeInterpreter
from encode.list.List import List


class EncodeList(List):
    """
        具有OneHot唯一编码的列表
    """

    def __init__(self, interpreter: EncodeInterpreter, records=None):
        """
        初始化
        :param interpreter:
        :param records:
        """
        if records is None:
            records = []

        super().__init__()
        # 数据
        self.records = records
        self.interpreter = interpreter

    def extend(self, records: list):
        """
        新增数据
        :param records:
        :return:
        """
        self.records.extend(records)
