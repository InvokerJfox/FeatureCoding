from encode.example.entity.displacement.entry.BaseEntry import BaseEntry
from encode.example.entity.displacement.entry.Coordinate import Coordinate


class PathNode(BaseEntry):
    def __init__(self, node_name: str, node_coordinates: list):
        super().__init__()
        self.node_name = node_name  # type:str
        self.node_coordinates = node_coordinates  # type:list[Coordinate]