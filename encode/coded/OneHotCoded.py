from numpy import array

from encode.coded.Coded import Coded
from encode.coder.OneHotCoder import OneHotCoder
from encode.list.CountingList import CountingList


class OneHotCoded(Coded):
    """
    用于存储独热编码后的数据
    注:1.输入值不允许重复(不可重定义)
    2.仅存储具有唯一性的数据
    """

    def __init__(self, coder: OneHotCoder):
        """
        初始化一个编码结果存储单元
        :param coder:编码表
        """
        super().__init__(coder)
        # 数据的多维编码(函数映射)结果,格式如:[[0,0,1],[1,0,0]]
        self.protect_coded = array(())
        # 多维编码(函数映射)的反向数据索引
        self.protect_coded_indexes = {}
