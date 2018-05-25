from numpy import array

from encode.coder.Coder import Coder
from encode.combiner.DefaultCombiner import DefaultCombiner
from encode.interpreter.Interpreter import Interpreter


class RouteCoder(Coder):
    """
    通过若干的关系(即"边/edge")将两个状态(即"点/vertex")进行连接，最终形成一个关系网络(即图/graph,这里用Route代替);
    图(graph)常用于求解最短距离问题,其核心输入参数之一为收益函数(gain function);
    收益函数使用的度量可以包含但不限于：路径的长度、可靠性、时延、带宽、负载等。
    """

    def __init__(self, identifier: Interpreter, combiner=DefaultCombiner):
        """
        初始化一个图关系编码表
        :param identifier: 识别器
        :param combiner: 组合器
        """
        super().__init__()
        # 数据识别器
        self.identifier = identifier  # type:Interpreter
        # 编码组合器
        self.combiner = combiner
        # 点编码原始数据，编码后数据根据索引查找
        self.vertex_descriptions = []
        # 点编码后的数据
        self.vertices = array(())
        # 点编码后的数据(唯一)倒索引
        self.vertex_indexes = {}
        # 边编码原始数据，编码后根据索引查找
        self.edge_descriptions = []
        # 边编码后数据
        self.edges = array(())
