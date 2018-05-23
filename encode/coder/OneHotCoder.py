from numpy import array

from encode.coder.Coder import Coder
from encode.combiner.DefaultCombiner import DefaultCombiner


class OneHotCoder(Coder):
    """
        单个对象的独热编码表
        1.值可以是具有唯一特性的数值,字符串等，满足3范式
        2.每一行表示一条记录,每一列表示一个维度，这些维度及其值是完全不相关的
        3.编码输入值不允许重复(不可重定义)
    """

    def __init__(self, dimensions: set, combiner=DefaultCombiner):
        """
        初始化一个独热编码表
        :param dimensions: 每一个编码对应的说明信息
        :param combiner: 组合器
        """
        super().__init__()
        # 进行编码的维度
        self.dimensions = dimensions
        # 编码组合器
        self.combiner = combiner
        # 原始数据
        self.descriptions = []
        # 编码表
        self.codes = array(())
        # 编码后的数据(唯一)倒索引
        self.code_indexes = {}
