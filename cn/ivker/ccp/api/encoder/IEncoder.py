from cn.ivker.ccp.utility.string import StringCombiner


class IEncoder:
    """
    编码器接口
    """

    @staticmethod
    def encode(records: list, combiner: StringCombiner) -> list:
        """
        编码
        :param records:
        :param combiner:
        :return:
        """
        pass

    @staticmethod
    def decode(codes: list, combiner: StringCombiner) -> list:
        """
        解码
        :param codes:
        :param combiner:
        :return:
        """
        pass

    @staticmethod
    def hash(records: list, combiner: StringCombiner) -> list:
        """
        哈希编码
        :param records:
        :param combiner:
        :return:
        """
        pass
