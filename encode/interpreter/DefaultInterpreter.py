from encode.interpreter.Interpreter import Interpreter


class DefaultInterpreter(Interpreter):
    def __init__(self, dimensions: list):
        """

        :param dimensions:
        """
        self.dimensions = dimensions

    def dimensions(self, record: dict) -> dict:
        r = {}
        for encode in self.dimensions:
            r[encode] = record[encode]
        return r
