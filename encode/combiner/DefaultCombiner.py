from encode.combiner.ICombiner import ICombiner


class DefaultCombiner(ICombiner):
    """
    默认的编码组合器
    """

    @staticmethod
    def combine(keys: list, sp="_") -> str:
        """
        基于分隔符组合字符串
        :param keys:
        :param sp:
        :return:
        """
        if len(keys) == 0:
            return ""
        else:
            res = keys[0]  # type:str

        for s in keys[1:]:
            res = res + sp + str(s)

        return res

    @staticmethod
    def separate(value: str, sp="_") -> list:
        """
        通过分隔符拆字符串
        :param value:
        :param sp:
        :return:
        """
        return value.split(sp)
