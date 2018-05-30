from encode.combiner.ICombiner import ICombiner


class IProjector:
    @staticmethod
    def project(records: list, dimensions: list, projects: list, combiner: ICombiner):
        pass

    @staticmethod
    def projecting(records: list, dimensions: list, benchmark: dict, projects: list, combiner: ICombiner):
        pass
