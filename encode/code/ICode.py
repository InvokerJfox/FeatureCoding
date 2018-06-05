from encode.combiner.ICombiner import ICombiner


class ICode:
    @staticmethod
    def code(record: dict, combiner: ICombiner) -> str:
        pass

    @staticmethod
    def hash(record: dict, combiner: ICombiner) -> str:
        pass
