from numpy.ma import zeros

from encode.coder.IterativeRouteCoder import IterativeRouteCoder


class IterativeRouteEncoder:
    """
    定义编码规模,对数据进行图编码(点+边)
    """

    @staticmethod
    def register(passport: str, vertex_features: list, edge_features: list, gain_function, selector_function,
                 vertex_features_code_key="feature", edge_features_code_key="feature") -> GraphCoder:

        """
        通过特征生成一个简单的独热编码器
        :param passport: 通行证(码),用于识别编码问题
        :param vertex_features: 图中"点"必要的特征集合(含说明)
        :param edge_features: 图中"边"必要的特征集合(含说明)
        :param gain_function: 基于"点"和"边"的特征计算出收益的函数
        :param selector_function: 基于收益结果进行迭代更新"点"和"边"的特征值函数
        :param vertex_features_code_key: "点"编译特征字段
        :param edge_features_code_key: "边"编译特征字段
        """

        # 取特征值:多个相同的特征会映射为同一个值
        vertex_features_codes = set()
        for vertex_feature in vertex_features:  # type:dict
            vertex_features_codes.add(vertex_feature[vertex_features_code_key])

        edge_features_codes = set()
        for edge_feature in edge_features:  # type:dict
            edge_features_codes.add(edge_feature[edge_features_code_key])

        return IterativeRouteCoder(passport, vertex_features, vertex_features_codes, edge_features, edge_features_codes,
                          gain_function, selector_function)

    @staticmethod
    def dots(coder: IterativeRouteCoder, data: list, code_keys: list) -> list:
        """
        输入"点"及其特征进行编码
        :param coder:
        :param data:list[dict]
        :param code_keys: data中要编码的keys
        :return:
        """
        data_size = len(data)
        dimension_size = len(code_keys)
        coded = zeros((data_size, dimension_size))
        features = coder.vertices  # type:list
        for cursor in range(data_size):
            for key in code_keys:
                key_index = features.index(key) if key in features else -1
                if key_index != -1:
                    coded[cursor, key_index] = data[cursor][key]
                else:
                    raise ValueError("key:%s is not in codes!" % key)

        return coded

    @staticmethod
    def edging(coder: IterativeRouteCoder, data: list, code_keys: list) -> list:
        """
        输入"边"及其特征进行编码
        :param coder:
        :param data:list[dict]
        :param code_keys: data中要编码的keys
        :return:
        """
        data_size = len(data)
        dimension_size = len(code_keys)
        coded = zeros((data_size, dimension_size))
        features = coder.edges  # type:list
        for cursor in range(data_size):
            for key in code_keys:
                key_index = features.index(key) if key in features else -1
                if key_index != -1:
                    coded[cursor, key_index] = data[cursor][key]
                else:
                    raise ValueError("key:%s is not in codes!" % key)

        return coded
