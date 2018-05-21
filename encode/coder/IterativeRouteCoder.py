class IterativeRouteCoder:
    """
    通过若干的关系(即"边/edge")将两个状态(即"点/vertex")进行连接，最终形成一个关系网络(即图/graph);
    图(graph)常用于求解最短距离问题,其核心输入参数之一为收益函数(gain function);
    收益函数使用的度量可以包含但不限于：路径的长度、可靠性、时延、带宽、负载等。
    """

    def __init__(self, passport: str, vertex_features: list, vertex_features_codes: set,
                 edge_features: list, edge_features_codes: set,
                 gain_function, selector_function):
        """
        初始化一个图关系编码表
        :param passport:通行证
        :param vertex_features:图中"点"必要的特征集合
        :param vertex_features_codes:图中"点"必要的特征编码
        :param edge_features:图中"边"必要的特征集合
        :param edge_features_codes:图中"点"必要的特征编码
        :param gain_function:基于"点"和"边"的特征计算出收益的函数
        :param selector_function:基于收益结果进行迭代更新"点"和"边"的特征值函数
        """
        super().__init__()
        self.passport = passport
        self.vertices = vertex_features_codes
        self.vertices_description = vertex_features
        self.edges = edge_features_codes
        self.edges_description = edge_features
        self.gain_function = gain_function
        self.selector_function = selector_function
