class IDecoding:
    """
    译码表
    """

    def feed(self, records: list):
        """
        输入学习数据
        :param records:
        :return:
        """
        pass

    def poison(self, indexes: list):
        """
        输入遗忘数据
        :param indexes:
        :return:
        """
        pass
