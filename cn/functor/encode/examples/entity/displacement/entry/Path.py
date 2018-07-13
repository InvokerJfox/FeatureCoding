from encode.example.entity.displacement.entry import PathNode
from encode.example.entity.displacement.entry.Coordinate import Coordinate

from cn.functor.encode.examples.entity.displacement.entry.BaseEntry import BaseEntry


class Path(BaseEntry):
    def __init__(self, path_name: str, source_node: PathNode, target_node: PathNode, path_distance: float,
                 traffic_capacity_index=None, traffic_path_type=None, path_height=None, path_width=None,
                 path_weight=None, path_coordinates=None, path_code=None):
        super().__init__()
        if path_coordinates is None:
            path_coordinates = []
        self.path_name = path_name  # type:str
        self.source_node = source_node  # type:PathNode
        self.target_node = target_node  # type:PathNode
        self.traffic_capacity_index = traffic_capacity_index  # type:int
        self.traffic_path_type = traffic_path_type  # type:str
        self.path_height = path_height  # type:float
        self.path_width = path_width  # type:float
        self.path_weight = path_weight  # type:float
        self.path_distance = path_distance  # type:float
        self.path_code = path_code  # type:int
        self.path_coordinates = path_coordinates  # type:list[Coordinate]
