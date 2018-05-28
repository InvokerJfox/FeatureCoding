from numpy import array

from encode.coded.Coded import Coded
from encode.coded.OneHotCoded import OneHotCoded
from encode.coder.MappingCoder import MappingCoder
from encode.list.CountingList import CountingList


class MappingCoded(Coded):
    """
    存储映射型独热编码的结果
    注:1.输入值不允许重复(不可重定义)
    2.仅存储具有唯一性的数据
    """

    def __init__(self, coder: MappingCoder, vertices: OneHotCoded):
        """
        初始化一个编码结果存储单元
        :param coder: 编码器
        :param vertices:编码
        """
        super().__init__(coder)
        # 用于解释基础状态的带点信息
        self.vertices = vertices
        # 基于基础状态形成的映射关系(映射结果为列表),格式:[[list,list][list,list]]
        self.edges = array(())
