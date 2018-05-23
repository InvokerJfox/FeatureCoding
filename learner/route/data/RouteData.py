import numpy as np
from numpy import array

from encode.coder.RouteCoder import RouteCoder
from encode.encoder.RouteEncoder import RouteEncoder


class RouteData:
    """
    用于存储路由(图)编码后的数据
    """

    def __init__(self, coder: RouteCoder):
        """
        初始化一个编码存储单元
        :param coder: 编码表
        """
        super().__init__()
        self.coder = coder  # 编码器
        self.vertices = array(())  # 编码后的点数据:{编码后状态值}
        self.vertex_descriptions = []  # 编码原点数据:{编码后数据的索引:原始数据}
        self.edges = array(())  # 编码后的边数据:{编码后状态值}
        self.edge_descriptions = []  # 编码点边数据:{编码后数据的索引:原始数据}

    def append_vertices(self, records: list):
        self.vertex_descriptions.extend(records)
        self.vertices = np.append(self.vertices, RouteEncoder.dots(self.coder, records))

    def append_edges(self, records: list):
        self.edge_descriptions.extend(records)
        self.vertices = np.append(self.vertices, RouteEncoder.edging(self.coder, records))
