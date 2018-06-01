from encode.code.DimensionCode import DimensionCode
from encode.interpreter.UniqueInterpreter import UniqueInterpreter
from encode.list.EncodeList import EncodeList


class UniqueList(EncodeList):
    def __init__(self, interpreter: UniqueInterpreter):
        super().__init__(interpreter)
        #  已存在数据字典表,及其对应的数据索引
        self.uniques = {}


def encode_to_unique(el: EncodeList) -> UniqueList:
    """
    将输入的EncodeList 添加唯一码成为 UniqueList
    :param el:
    :return:
    """
    # 提取解释器 & 数据
    interpreter = UniqueInterpreter(el.interpreter.encode_dimensions,
                                    el.interpreter.feature_dimensions)
    records = el.records
    # 结果
    l = []
    uniques = {}

    for record in records:  # type:dict
        # 取唯一码，不存在时用组合器生成
        unique = interpreter.unique(record)
        if unique is None:
            # 提取编码并生成唯一码存储
            encodes = interpreter.encodes(record)
            unique = DimensionCode.code(encodes)
            record[interpreter.unique_dimension] = unique

        # 判断唯一码是否冲突,冲突时提示
        if unique in uniques:
            print("WARMING: UniqueEncoder got duplicate unique value:[%s]" % unique)
        else:
            uniques[unique] = len(l)
            l.extend([record])

    ul = UniqueList(interpreter)
    ul.records = l
    ul.uniques = uniques

    return ul
