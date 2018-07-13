from cn.ivker.encode.examples.entity.displacement.entry.BaseEntry import BaseEntry


class Map(BaseEntry):
    def __init__(self, map_id: int, map_name: str, map_code=None, boundary_area=None, areas=None, positions=None,
                 path_node=None):
        """
        initial a map
        :param map_name: identify name
        :param map_code: encode to a encode id
        :param boundary_area:the boundary of this map,used to limited the coordinate of the displacement ,area and path.
        None means the map is infinite.
        :param areas: in this map
        :param positions: in this map
        """
        super().__init__()
        self.map_id = map_id
        self.name = map_name  # type:str
        self.map_code = map_code  # type:int
        self.boundary_area = boundary_area  # type:Area
        if areas is None:
            areas = []
        self.areas = areas  # type:list[Area]
        if positions is None:
            positions = []
        self.positions = positions  # type:list[Position]
        if path_node is None:
            path_node = []
        self.path_node = path_node
