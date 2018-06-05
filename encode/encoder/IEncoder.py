from encode.combiner.ICombiner import ICombiner


class IEncoder:
    """
    编码器接口
    """

    @staticmethod
    def encode(record: dict, combiner: ICombiner) -> str:
        """
        编码
        :param record:
        :param combiner:
        :return:
        """
        pass

    @staticmethod
    def decode(code: str, combiner: ICombiner) -> dict:
        """
        解码
        :param code:
        :param combiner:
        :return:
        """
        pass

    @staticmethod
    def hash(record: dict, combiner: ICombiner) -> str:
        """
        哈希编码
        :param record:
        :param combiner:
        :return:
        """
        pass
