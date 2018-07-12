from encode.example.entity.displacement.entry.Coordinate import Coordinate
from encode.example.entity.displacement.entry.LinkToPathNode import LinkToPathNode

from cn.jfoxx.encode.examples.entity.displacement.entry.BaseEntry import BaseEntry


class Area(BaseEntry):
    def __init__(self, area_id: int, area_name: str, min_height: float, max_height: float,
                 boundary_coordinate=None, link_to_path_node=None, area_code=None):
        super().__init__()
        self.area_id = area_id
        if boundary_coordinate is None:
            boundary_coordinate = []
        self.area_name = area_name  # type:str
        self.min_height = min_height  # type:float
        self.max_height = max_height  # type:float
        self.boundary_coordinate = boundary_coordinate  # type:list[Coordinate]
        self.link_to_path_node = link_to_path_node  # type:LinkToPathNode
        self.area_code = area_code  # type:int
