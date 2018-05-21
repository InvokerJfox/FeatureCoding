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
        self.data = []

    def append(self, data: list, start_key="from", target_key="to"):
        """
        添加新数据
        :param data:原始数据
        :param start_key:起始映射维度
        :param target_key:目标映射维度
        :return:
        """
        self.description.append(data)
        self.data.append(MappingOneHotEncoder.coding(self.coder, data, start_key=start_key, target_key=target_key))
