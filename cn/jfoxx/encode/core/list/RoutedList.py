from numpy import array

from cn.jfoxx.encode import Encoded


class RouteEncoded(Encoded):
    """
    路由器编码结果
    """

    def __init__(self):
        """
        初始化编码结果存储单元
        """
        super().__init__()
        # 存储基于状态结果(UniqueCoding.uniques)的映射关系(映射结果为列表),格式:[[list,list][list,list]]
        self.routes = array(())
