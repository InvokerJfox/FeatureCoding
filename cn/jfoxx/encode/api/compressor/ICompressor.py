from cn.jfoxx.encode import Vector


class ICompressor:
    """
    数据压缩器接口
    """

    @staticmethod
    def compress(records: Vector) -> list:
        """
        对数据进行压缩
        :param records:
        :return:
        """
        pass
