from cn.jfoxx.encode.utility import ICombiner


class IEncoder:
    """
    编码器接口
    """

    @staticmethod
    def encode(records: list, combiner: ICombiner) -> list:
        """
        编码
        :param records:
        :param combiner:
        :return:
        """
        pass

    @staticmethod
    def decode(codes: list, combiner: ICombiner) -> list:
        """
        解码
        :param codes:
        :param combiner:
        :return:
        """
        pass

    @staticmethod
    def hash(records: list, combiner: ICombiner) -> list:
        """
        哈希编码
        :param records:
        :param combiner:
        :return:
        """
        pass
