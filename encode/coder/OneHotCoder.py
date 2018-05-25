from encode.coder.Coder import Coder
from encode.combiner.DefaultCombiner import DefaultCombiner
from encode.compressor.CountingCompressor import CountingCompressor
from encode.list.CountingList import CountingList
from encode.projector.DimensionProjector import DimensionProjector


class OneHotCoder(Coder):
    """
        单个对象的独热编码表
        1.值可以是具有唯一特性的数值,字符串等，满足3范式
        2.每一行表示一条记录,每一列表示一个维度，这些维度及其值是完全不相关的
    """

    def __init__(self, compressor: CountingCompressor, projector: DimensionProjector, combiner=DefaultCombiner):
        """
        初始化一个独热编码表
        :param compressor: 压缩器:基于解释压缩数据
        :param projector:投影仪:将数据进行投影的方式
        :param combiner: 组合器:将数据组合为编码唯一码
        """
        super().__init__()
        # 数据压缩器
        self.compressor = compressor
        # 编码投影仪
        self.projector = projector
        # 编码组合器
        self.combiner = combiner
        # 原始数据
        self.descriptions = CountingList(compressor)
        # 多维编码(函数映射)
        self.protects = []
        # 反向索引,多维编码对应维度的索引
        self.protect_indexes = {}
        # 唯一编码
        self.codes = []
        # 反向索引,唯一编码(高维哈希)对应记录的索引
        self.code_indexes = {}
