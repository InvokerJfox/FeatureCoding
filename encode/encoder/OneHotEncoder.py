from numpy import zeros

from encode.coder.OneHotCoder import OneHotCoder
from encode.encoder.Encoder import Encoder
from encode.list.UniqueList import UniqueList
from encode.projector.DimensionProjector import DimensionProjector


class OneHotEncoder(Encoder):
    """
        定义编码规模,对数据进行one-hot编码(0/1编码)
    """

    @staticmethod
    def coder(records: UniqueList, identifier=None, coder=None, projector=DimensionProjector) -> OneHotCoder:
        """
        通过特征生成一个简单的独热编码器,coder和code_dimensions至少一个不为空
        :param records: 编码的所有记录(含说明)
        :param identifier: 识别器
        :param coder: 编码器
        :param projector: 投影仪
        :return:
        """
        # coder和code_dimensions其一不为空
        if coder is None:
            if identifier is not None:
                coder = OneHotCoder(identifier, projector)
            else:
                raise ValueError("'coder' and 'identifier & projector' at least one is not empty")

        # 获取多维投影仪
        projector = coder.projector  # type:DimensionProjector
        # 获取编码维度
        encode_dimensions = coder.identifier.encode_dimensions
        # 获取原多维编码
        protects = coder.protects  # type:list

        # 对数据进行多维编码 & 更新
        projector.mapping(records, encode_dimensions, protects)

        # 重置反射索引
        coder.code_indexes = dict(zip(protects, range(len(protects))))

        # 添加唯一索引
        onehot_dimension = coder.identifier.onehot_dimension
        new_codes = map(lambda x: x[onehot_dimension], records)
        coder.codes.extend(new_codes)

        # 追加记录
        coder.descriptions.extend(records)

        return coder

    @staticmethod
    def coding(coder: OneHotCoder, records: list) -> list:
        """
        将数据生成独热编码，并将其作为唯一标识放入数据中
        :param coder:
        :param records:list[dict]
        :return:
        """
        # 映射码
        protects = coder.protects  # type:list
        # 编码维度
        code_dimensions = coder.identifier.encode_dimensions
        # 映射函数
        projector = coder.projector
        # 规模
        hashes_size = len(protects)
        data_size = len(records)

        # 编码结果
        coded = zeros((data_size, hashes_size))
        # 遍历所有数据
        for record_index in range(data_size):
            record = records[record_index]  # type:dict
            # 选取所有要编码的字段
            # 依次对比编码对象,匹配成功则匹配下一个
            hashes_index = 0
            for code_dimension in code_dimensions:
                # 编码:
                code = coder.combiner.combine([code_dimension, str(record[code_dimension])])
                while hashes_index < hashes_size:
                    # 若值与编码匹配则标记，且不再查找下一编码
                    if code == protects[hashes_index]:
                        coded[record_index, hashes_index] = 1
                        break
                    hashes_index += 1

        return coded.tolist()
