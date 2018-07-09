from encode.interpreter.Interpreter import Interpreter


class List:
    """
    数据列表
    """

    def __init__(self, interpreter: Interpreter):
        super().__init__()
        # 数据
        self.records = []
        # 数据解释器
        self.interpreter = interpreter

    def extend(self, records: list) -> list:
        """
        新增数据,并放回新增数据所处索引
        :param records:
        :return:返回更新索引
        """
        # 新增数据
        self.records.extend(records)
        # 返回增量索引
        l = len(records)
        total = len(self.records)
        return range(total - l, total)

    def remove(self, indexes: list):
        """
        移除数据
        :param indexes:
        :return:
        """
        for index in indexes:
            self.records.remove(index)
