class ILearner:
    """
    译码表
    """

    def __init__(self):
        super().__init__()
        self.records = []

    def feed(self, records: list):
        """
        输入学习数据
        :param records:
        :return:
        """
        pass

    def leak(self, indexes: list):
        """
        输入遗忘数据
        :param indexes:
        :return:
        """
        pass
