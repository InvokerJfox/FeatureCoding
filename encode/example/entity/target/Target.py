class Target:
    def __init__(self, targets_id: int, feature_origin_object: list, feature_target_object: list,
                 feature_origin_code: list, feature_target_code: list):
        super().__init__()
        self.test_dimension_change = test_dimension_change  # type:list[list[int,int]]
