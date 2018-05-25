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
        super().__init__()
        self.coder = coder  # 编码器
        self.descriptions = CountingList(coder.compressor)  # 编码原数据及编码结果
        self.coded = array(())  # 编码后的数据,格式如:[[0,0,1],[1,0,0]]
        self.coded_indexes = {}  # 通过编码唯一码反射原数据/编码数据索引,编码值一
