from encode.coded.OneHotCoded import OneHotCoded
from encode.coder.Coder import Coder
from encode.compressor.CountingCompressor import CountingCompressor


class MappingCoder(Coder):
    """
    映射编码表
    1.值可以是具有唯一特性的数值,字符串等，满足3范式
    2.每一行表示一条记录,每一列表示一个维度，这些维度及其值是完全不相关的
    """

    def __init__(self, compressor: CountingCompressor, vertices: OneHotCoded):
        """
        初始化一个映射编码表
        :param compressor: 压缩器:压缩数据
        :param vertices:点(状态)数据
        """
        super().__init__(compressor)
        # 用于解释基础状态的带点信息
        self.vertices = vertices
        # 点(状态)的唯一编码
        self.vertex_uniques = []
        # 点(状态)码反向索引,表示其所在的索引
        self.vertex_unique_indexes = {}
