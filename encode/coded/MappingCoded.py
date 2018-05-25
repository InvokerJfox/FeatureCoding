from numpy import array

from encode.coded.Coded import Coded
from encode.coder.MappingCoder import MappingCoder
from encode.list.CountingList import CountingList


class MappingCoded(Coded):
    """
    存储映射型独热编码的结果
    注:1.输入值不允许重复(不可重定义)
    2.仅存储具有唯一性的数据
    """

    def __init__(self, coder: MappingCoder):
        """
        初始化一个编码结果存储单元
        :param coder: 编码表
        """
        super().__init__()
        self.coder = coder  # 编码器
        self.descriptions = CountingList(coder.compressor)  # 编码原数据:{编码后数据的索引:原始数据}
        self.states = []  # 用于连接的基础状态(状态唯一编码)
        self.coded = array(())  # 基于基础状态形成的映射关系(映射结果为列表),格式:[[list,list][list,list]]
