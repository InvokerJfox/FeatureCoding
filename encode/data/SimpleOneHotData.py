from encode.coder.SimpleOneHotCoder import SimpleOneHotCoder
from encode.encoder.SimpleOneHotEncoder import SimpleOneHotEncoder


class SimpleOneHotData:
    """
    用于存储独热编码后的数据
    """

    def __init__(self, coder: SimpleOneHotCoder, data: list, code_dict: str):
        """

        :param coder:
        :param data:
        :param code_dict:
        """
        super().__init__()
        self.coder = coder
        self.description = data
        self.data = SimpleOneHotEncoder.coding(coder, data, code_dict)

    def append(self, other):
        pass

    def __add__(self, other):
        self.append(other)
