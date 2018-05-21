import numpy as np
from numpy import array

from encode.coder.MappingOneHotCoder import MappingOneHotCoder
from encode.encoder.MappingOntHotEncoder import MappingOneHotEncoder


class MappingOneHotData:
    """
    存储映射型独热编码的结果
    """

    def __init__(self, coder: MappingOneHotCoder):
        """
        初始化一个编码结果存储单元
        :param coder: 编码表
        """
        super().__init__()
        self.coder = coder
        self.description = []
        self.data = array(())

    def append(self, data: list):
        """
        添加新数据
        :param data:原始数据
        :return:
        """
        self.description.extend(data)
        self.data = np.append(self.data, MappingOneHotEncoder.coding(self.coder, data))
