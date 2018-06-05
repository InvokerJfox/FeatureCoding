from numpy import array


class IterativeRouteCoder:
    """
    通过若干的关系(即"边/edge")将两个状态(即"点/vertex")进行连接，最终形成一个关系网络(即图/graph,这里用Route代替);
    图(graph)常用于求解最短距离问题,其核心输入参数之一为收益函数(gain function);
    收益函数使用的度量可以包含但不限于：路径的长度、可靠性、时延、带宽、负载等。
    """

    def __init__(self, passport: str, vertex_state_codes: dict, vertex_feature_codes: set, vertex_descriptions: list,
                 edge_link_codes: dict, edge_feature_codes: set, edge_descriptions: list, gain_function,
                 selector_function):
        """
        初始化一个图关系编码表
        :param passport:通行证
        :param vertex_state_codes:图中"点"的状态码
        :param vertex_feature_codes:图中"点"的特征码
        :param vertex_descriptions:图中"点"的描述
        :param edge_link_codes:图中"边"的状态码
        :param edge_feature_codes:图中"边"的特征码
        :param edge_descriptions:图中"边"的描述
        :param gain_function:基于"点"和"边"的特征计算出收益的函数
        :param selector_function:基于收益结果进行迭代更新"点"和"边"的特征值函数
        """
        super().__init__()
        self.passport = passport
        self.vertices = vertex_state_codes
        self.vertex_features = vertex_feature_codes
        self.vertex_descriptions = vertex_descriptions
        self.edges = edge_link_codes
        self.edges_features = edge_feature_codes
        self.edges_descriptions = edge_descriptions
        self.gain_function = gain_function
        self.selector_function = selector_function
