from numpy import array

from encode.coded.UniqueCoded import UniqueCoded
from encode.interpreter.UniqueInterpreter import UniqueInterpreter


class ProjectCoded(UniqueCoded):
    """
    投影编码结果
    """

    def __init__(self, interpreter: UniqueInterpreter):
        """
        初始化一个编码结果存储单元
        :param interpreter: 解释器
        """
        super().__init__(interpreter)
        # 数据的多维编码(函数映射)结果,格式如:[[0,0,1],[1,0,0]]
        self.protect_uniques = array(())
