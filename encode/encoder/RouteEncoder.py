from numpy import zeros
from numpy import array
from encode.coder.RouteCoder import RouteCoder
from encode.encoder.IEncoder import IEncoder


class RouteEncoder(Encoder):
    """
    定义编码规模,对数据进行图编码(点+边)
    """

    @staticmethod
    def coder(vertices: list, identifier=None, coder=None) -> RouteCoder:

        """
        对"点"和"边"设计编码器

        :param vertices: 编码的所有点(含说明)
        :param identifier: 识别器
        :param coder: 编码器
        """
        # coder和code_dimensions其一不为空
        if coder is None:
            if identifier is not None:
                coder = RouteCoder(identifier)
            else:
                raise ValueError(
                    "'coder' and 'interpreter',at least one is not empty")

        # 对点进行编码
        # 获取编码维度
        vertex_dimensions = coder.identifier.vertex_state_code_keys
        # 获取原编码 & 原编码索引
        vertex_codes = coder.vertices.tolist()  # type:list
        vertex_code_indexes = coder.vertex_indexes  # type:dict

        # 访问每个新记录,当不存在时,添加该编码及反射索引
        for vertex_index in range(len(vertices)):
            vertex = vertices[vertex_index]  # type:dict
            for dimension_key in vertex_dimensions:  # type:str
                # 编码
                code = coder.combiner.combine([dimension_key, str(vertex[dimension_key])])
                # 判断是否存在/添加
                if code not in vertex_code_indexes:
                    vertex_codes.extend([code])

        # 存储
        coder.vertices = array(vertex_codes)

        # 重置反射索引
        coder.vertex_indexes = dict(zip(vertex_codes, range(len(vertex_codes))))

        # 追加记录
        coder.vertex_descriptions.extend(vertices)

        return coder

    @staticmethod
    def dots(coder: RouteCoder, records: list) -> list:
        """
        输入"点"及其特征进行编码
        :param coder: 编码器
        :param records:待编码记录 list[dict]
        :return:
        """
        # 已存在编码
        vertex_codes = coder.vertices
        # 编码维度
        vertex_dimensions = coder.identifier.vertex_state_code_keys

        # 规模
        codes_size = len(vertex_codes)
        data_size = len(records)

        # 编码结果
        vertex_coded = zeros((data_size, codes_size))

        # 遍历所有数据
        for record_index in range(data_size):
            record = records[record_index]  # type:dict
            # 选取所有要编码的字段
            # 依次对比编码对象,匹配成功则匹配下一个
            codes_index = 0
            for code_dimension in vertex_dimensions:
                # 编码格式:维度+值
                value = code_dimension + str(record[code_dimension])
                while codes_index < codes_size:
                    # 若值与编码匹配则标记，且不再查找下一编码
                    if value == vertex_codes[codes_index]:
                        vertex_coded[record_index, codes_index] = 1
                        break
                    codes_index += 1

        return vertex_coded.tolist()

    @staticmethod
    def edging(coder: RouteCoder, edges: list) -> list:
        """
        对已输入的"点",输入"边"进行映射编码
        :param coder:
        :param edges:list[dict]
        :return:
        """
        # 已存在编码
        codes = coder.edges  # type:array
        # 编码维度
        edge_start = coder.identifier.edge_start_key
        edge_target = coder.identifier.edge_target_key

        # 规模
        codes_size = len(codes)
        data_size = len(edges)

        # 编码结果:
        # 新增编码_状态变化矩阵:
        # 行:起始点(索引匹配点索引)
        # 列:目标点(索引匹配点索引)
        # 值:边列表(可以存在多种达到方式)
        coded = zeros((data_size, codes_size), dtype=list)
        # 遍历所有数据
        for edge in edges:
            # 选取起始态与目标态表示的位置,将该链接插入
            # 连接信息:起始点码和状态点码
            start_code = edge_start + str(edge[edge_start])
            target_code = edge_target + str(edge[edge_target])

            # 获取对应坐标

        return coded
