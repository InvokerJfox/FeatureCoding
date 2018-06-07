class Interpreter:
    def __init__(self, dimensions=None):
        """

        :param dimensions:
        """
        if dimensions is None:
            dimensions = []
        self.dimensions = dimensions

    def dimensions(self, record: dict) -> dict:
        r = {}
        for encode in self.dimensions:
            r[encode] = record[encode]
        return r
