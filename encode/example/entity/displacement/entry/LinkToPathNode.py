from encode.example.entity.displacement.entry.PathNode import PathNode


class LinkToPathNode:
    def __init__(self, link_id: int, link_name: str, link_path_node: PathNode, link_as_a_path=None, link_code=None):
        super().__init__()
        self.link_id = link_id
        self.link_name = link_name  # type:str
        self.link_path_node = link_path_node  # type:PathNode
        self.link_as_a_path = link_as_a_path  # type:Path
        self.link_code = link_code  # type:int
