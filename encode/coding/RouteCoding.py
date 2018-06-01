from encode.coding.UniqueCoding import UniqueCoding


class LinkCoding(UniqueCoding):
    """
    编码器的译码

    """

    def __init__(self, vertices: UniqueCoding):
        """
        初始化一个映射译码表
        :param vertices:点(状态)数据
        """
        super().__init__()
        # 用于解释基础状态的带点信息
        self.vertices = vertices
        # 点(状态)的唯一编码,及其对应的数据索引
        self.vertex_uniques = {}
