from encode.coding.UniqueCoding import UniqueCoding
from encode.interpreter.UniqueInterpreter import UniqueInterpreter
from encode.projector.DimensionProjector import DimensionProjector


class ProjectCoding(UniqueCoding):
    """
    编码器的译码

    """

    def __init__(self, interpreter: UniqueInterpreter, projector: DimensionProjector):
        """
        初始化一个独热编码表
        :param interpreter:数据解释器
        :param projector:投影仪:将数据进行投影的方式
        """
        super().__init__(interpreter)
        # 编码投影仪
        self.projector = projector
        # 多维编码(函数映射),及其对应的数据索引
        self.protects = {}
