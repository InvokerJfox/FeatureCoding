from cn.ccp.encode.examples.entity.displacement.entry.BaseEntry import BaseEntry


class Coordinate(BaseEntry):
    def __init__(self, x: float, y: float, z=None):
        super().__init__()
        self.x = x  # type:float
        self.y = y  # type:float
        self.z = z  # type:float
