import numpy as np
from numpy import array

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
        self.data = array(())
        self.description = []

    def append(self, data: list):
        """
        添加新数据
        :param data:待新增数据
        :return:
        """
        self.description.extend(data)
        self.data = np.append(self.data, SimpleOneHotEncoder.coding(self.coder, data))
