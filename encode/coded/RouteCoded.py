from numpy import array

from encode.coder.RouteCoder import RouteCoder
from encode.coded.Coded import Coded
from encode.encoder.RouteEncoder import RouteEncoder


class RouteCoded(Coded):
    """
    用于存储路由(图)编码后的数据
    注:1.输入值不允许重复(不可重定义)
    2.仅存储具有唯一性的数据
    """

    def __init__(self, coder: RouteCoder):
        """
        初始化一个编码存储单元
        :param coder: 编码表
        """
        super().__init__()
        self.coder = coder  # 编码器
        self.vertex_descriptions = []  # 编码原点数据:{编码后数据的索引:原始数据}
        self.vertices = array(())  # 编码后的点数据:{编码后状态值}
        self.vertex_indexes = {}  # 通过编码唯一码反射原数据/编码数据索引
        self.edge_descriptions = []  # 编码点边数据:{编码后数据的索引:原始数据}
        self.edges = array(())  # 编码后的边数据:{编码后状态值}

    def append_vertices(self, records: list):
        """
        添加新的点
        :param records:待新增数据
        :return:
        """
        # 新增数据
        self.vertex_descriptions.extend(records)
        # 新增编码结果
        coded = self.vertices.tolist()  # type:list
        coded.extend(RouteEncoder.dots(self.coder, records))
        self.vertices = array(coded, dtype=int)

        # 重置反射索引
        onehots = map(lambda x: x[self.coder.identifier.onehot_dimension], records)
        self.vertex_indexes = dict(zip(list(onehots), range(len(records))))

        # 若出现重复定义:索引数不等于数据量，则抛出异常
        if len(records) != len(self.vertex_indexes):
            raise ValueError('input repeat records into coder')

    def append_edges(self, records: list):
        """
        添加新的边.注:边是点的拓展,不存点的边是非法的
        :param records:
        :return:
        """
        # 新增结果
        self.edge_descriptions.extend(records)
        # 新增编码结果
