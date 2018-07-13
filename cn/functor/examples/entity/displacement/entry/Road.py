from encode.example.entity.displacement.entry.Coordinate import Coordinate

from cn.functor.encode.examples.entity.displacement.entry.Area import Area


class Road:
    """
        The class has expired and replaced by <path> class.
    """

    def __init__(self, road_id: int, road_name: str, source_area: Area, target_area: Area, road_distance: float,
                 traffic_capacity_index=None, traffic_road_type=None, road_height=None, road_width=None,
                 road_weight=None, road_coordinates=None, road_code=None):
        super().__init__()
        self.road_id = road_id
        if road_coordinates is None:
            road_coordinates = []
        self.road_name = road_name  # type:str
        self.source_node = source_area  # type:Area
        self.target_node = target_area  # type:Area
        self.traffic_capacity_index = traffic_capacity_index  # type:int
        self.traffic_road_type = traffic_road_type  # type:str
        self.road_height = road_height  # type:float
        self.road_width = road_width  # type:float
        self.road_weight = road_weight  # type:float
        self.road_distance = road_distance  # type:float
        self.road_code = road_code  # type:int
        self.road_coordinates = road_coordinates  # type:list[Coordinate]
