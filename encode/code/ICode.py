from encode.combiner.ICombiner import ICombiner


class ICode:
    @staticmethod
    def code(record: dict, combiner: ICombiner) -> str:
        pass

    def hash(self):
        pass
