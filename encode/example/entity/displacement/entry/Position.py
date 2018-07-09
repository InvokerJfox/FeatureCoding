from encode.feature.displacement import BaseEntry
from encode.feature.displacement import Coordinate
from encode.feature.displacement import LinkToPathNode


class Position(BaseEntry):
    def __init__(self, position_id: int, position_name: str, coordinate: Coordinate,
                 link_to_path_area=None, position_code=None):
        super().__init__()

        self.position_id = position_id
        self.position_name = position_name  # type:str
        self.coordinate = coordinate  # type:Coordinate
        self.link_to_path_area = link_to_path_area  # type:LinkToPathNode
        self.position_code = position_code  # type:int
