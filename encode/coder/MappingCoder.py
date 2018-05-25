from encode.coder.Coder import Coder
from encode.combiner.DefaultCombiner import DefaultCombiner
from encode.compressor.CountingCompressor import CountingCompressor


class MappingCoder(Coder):
    """
    映射编码表
    1.值可以是具有唯一特性的数值,字符串等，满足3范式
    2.每一行表示一条记录,每一列表示一个维度，这些维度及其值是完全不相关的
    """

    def __init__(self, compressor: CountingCompressor, combiner=DefaultCombiner):
        """
        初始化一个映射编码表
        :param compressor: 压缩器:压缩数据
        :param combiner: 组合器:将数据组合为编码唯一码
        """
        super().__init__()
        # 数据压缩器
        self.compressor = compressor
        # 编码组合器
        self.combiner = combiner
        # 原始数据
        self.descriptions = []
        # 状态数据(唯一编码)
        self.states = []
        # 连接结果唯一编码
        self.codes = []
        # 反向索引,连接结果唯一码对应记录索引:如{"a→b":36}
        self.codes_indexes = {}
