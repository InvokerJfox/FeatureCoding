from encode.coder.SimpleOneHotCoder import SimpleOneHotCoder
from encode.encoder.SimpleOneHotEncoder import SimpleOneHotEncoder


class SimpleOneHotData:
    """
    用于存储独热编码后的数据
    """

    def __init__(self, coder: SimpleOneHotCoder):
        """
        初始化一个编码结果存储单元
        :param coder:编码表
        """
        super().__init__()
        self.coder = coder
        self.description = []
        self.data = []

    def append(self, data: list):
        """
        添加新数据
        :param data:原始数据
        :return:
        """
        self.description.append(data)
        self.data.append(SimpleOneHotEncoder.coding(self.coder, data))
