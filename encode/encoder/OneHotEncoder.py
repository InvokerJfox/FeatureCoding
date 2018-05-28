from numpy import array

from encode.coded.OneHotCoded import OneHotCoded
from encode.coder.OneHotCoder import OneHotCoder
from encode.encoder.Encoder import Encoder
from encode.list.CountingList import CountingList
from encode.projector.DimensionProjector import DimensionProjector


class OneHotEncoder(Encoder):
    """
        定义编码规模,对数据进行one-hot编码(0/1编码)
    """

    @staticmethod
    def coder(records: CountingList, coder=None, projector=DimensionProjector) -> OneHotCoder:
        """
        通过特征生成一个简单的独热编码器,coder和code_dimensions至少一个不为空
        可增量编译，但增量数据在全局数据中仍具有唯一性
        :param records: 增量编码记录(与原数据不相关)
        :param coder: 编码器
        :param projector: 投影仪
        :return:
        """
        # coder和code_dimensions其一不为空
        if coder is None:
            coder = OneHotCoder(records.compressor, projector)
        else:
            # 增量更新时，仅处理增量数据
            records = coder.descriptions.increment(records)
        # 待编码数据
        data = records.tolist()
        # 获取多维投影仪
        projector = coder.projector  # type:DimensionProjector
        # 获取已存在多维编码
        protects = coder.protects  # type:list
        # 获取编码维度
        encode_dimensions = coder.compressor.interpreter.encode_dimensions  # type:list

        # 对新数据进行多维编码 & 更新
        projector.mapping(data, encode_dimensions, protects)

        # 重置多维反射索引
        coder.protect_indexes = dict(zip(protects, range(len(protects))))

        # 添加唯一索引
        onehot_dimension = coder.compressor.interpreter.onehot_dimension
        new_codes = map(lambda x: x[onehot_dimension], data)
        coder.codes.extend(new_codes)

        # 重置多维反射索引
        coder.code_indexes = dict(zip(coder.codes, range(len(coder.codes))))

        # 追加记录
        coder.descriptions.extend(data)

        return coder

    @staticmethod
    def coding(records: CountingList, coder: OneHotCoder, coded=None) -> OneHotCoded:
        """
        将数据生成独热编码，并将其作为唯一标识放入数据中
        :param records:
        :param coder:
        :param coded:
        :return:
        """
        # 不存在则初始化编码结果
        if coded is None:
            coded = OneHotCoded(coder)
        # 待处理数据
        data = records.tolist()
        # 获取多维投影仪
        projector = coder.projector
        # 获取已存在多维编码
        protect_indexes = coder.protect_indexes  # type:dict
        # 获取编码维度
        encode_dimensions = coder.compressor.interpreter.encode_dimensions  # type:list
        # 获取已存在数据
        cd = coded.coded.tolist()  # type:array

        # 对所有新数据进行编码
        projector.match(data, encode_dimensions, protect_indexes, cd)

        # 存储编码结果
        coded.coded = array(cd, dtype=int)

        # 重置反射索引
        onehots = map(lambda x: x[coder.compressor.interpreter.onehot_dimension], data)
        coded.coded_indexes = dict(zip(list(onehots), range(len(data))))

        # 增加新增数据
        coded.descriptions = records

        return coded