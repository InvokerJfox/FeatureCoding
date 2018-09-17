from cn.ivker.ccp.encode.core.interpreter.Interpreter import Interpreter


class DID:
    """
    维度解释数据集(dimension interpret dataset),
    """

    def __init__(self, interpreter: Interpreter):
        super().__init__()
        # 数据
        self.records = []  # type:list[dict]
        # 数据解释器
        self.interpreter = interpreter

    def get(self):
        pass

    def extend(self, records: list):
        """
        新增数据,并放回新增数据所处索引
        :param records:
        :return:
        """
        # 新增数据
        self.records.extend(records)

    def remove(self, value):
        """
        移除数据
        :param value:
        :return:
        """
        self.records.remove(value)

    def removeAt(self, index: int):
        """
        移除数据
        :param index:
        :return:
        """
        del self.records[index]
