from numpy import array

from encode.coded.UniqueCoded import UniqueCoded
from encode.interpreter import RouteInterpreter


class RouteCoded(UniqueCoded):
    """
    路由器编码结果
    """

    def __init__(self, interpreter: RouteInterpreter):
        """
        初始化编码结果存储单元
        :param interpreter: 维度解释器
        """
        super().__init__(interpreter)
        # 存储基于状态结果(UniqueCoding.uniques)的映射关系(映射结果为列表),格式:[[list,list][list,list]]
        self.routes = array(())
