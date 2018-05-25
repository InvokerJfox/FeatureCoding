from numpy import array

from encode.coder.MappingCoder import MappingCoder
from encode.encoder.Encoder import Encoder
from encode.list.CountingList import CountingList


class MappingEncoder(Encoder):
    """
        定义编码规模,对数据进行映射型one-hot编码
        1.首先将所有状态基于压缩器进行唯一编码(onehotid)
        2.基于这些状态的唯一编码，建立连接关系编码(MappingCoder)并生成连接结果(MappingCoded)

    """

    @staticmethod
    def coder(records: CountingList, identifier=None, coder=None) -> MappingCoder:
        """
        通过特征生成一个映射型编码器
        :param records: 增量编码记录(与原数据不相关)
        :param identifier: 识别器
        :param coder: 编码器
        :return:
        """
        if coder is None:
            if identifier is not None:
                coder = MappingCoder(identifier)
            else:
                raise ValueError("'coder' and 'interpreter & projector' at least one is not empty")
        else:
            # 增量更新时，仅处理增量数据
            records = coder.descriptions.increment(records)

        # 获取编码维度
        start_dimension = coder.compressor.interpreter.start_dimension
        target_dimension = coder.compressor.interpreter.target_dimension

        # 对所有状态进行唯一编码


        # 重置多维反射索引
        coder.protect_indexes = dict(zip(protects, range(len(protects))))

        # 添加唯一索引
        onehot_dimension = coder.identifier.onehot_dimension
        new_codes = map(lambda x: x[onehot_dimension], records)
        coder.codes.extend(new_codes)

        # 重置多维反射索引
        coder.code_indexes = dict(zip(coder.codes, range(len(coder.codes))))

        # 追加记录
        coder.descriptions.extend(records)

        return coder

        # 追加记录
        coder.descriptions.extend(records)
        # 获取编码维度
        start_key = coder.start_key
        target_key = coder.target_key
        # 取特征值:key为start与target的合并，value为start/target分别值
        codes = coder.codes.tolist()  # type:list
        # 每个记录
        for value in records:  # type:dict
            start = str(value[start_key])
            target = str(value[target_key])
            # 编码格式:start+v(start)+target+v(target)
            code = start_key + start + target_key + target
            codes.extend([code])

        # 更新
        coder.codes = array(codes)
        return coder

    @staticmethod
    def coding(coder: MappingCoder, state: list, mapping: list) -> list:
        """
        基于状态及映射关系进行编码效验并返回编码结果
        :param coder:
        :param state:
        :param mapping:list[dict]
        :return:
        """
        codes = coder.codes
        # 编码维度
        start_key = coder.start_key
        target_key = coder.target_key
        # 编码结果
        coded = array((len(state), len(codes)))

        # 遍历所有数据
        for record in records:  # type:dict
            start = str(record[start_key])
            target = str(record[target_key])
            # 编码格式:start+v(start)+target+v(target)
            key = start_key + start + target_key + target
            if key in codes:
                result.setdefault(key, {start_key: start, target_key: target})
            else:
                raise ValueError("key(%s) doesn't in dict(%s)!" % (key, codes))

        return result

    def append(self, records: list):
        """
        添加新的状态
        :param records:待新增的状态数据
        :return:
        """
        # 新增编码结果
        coded = self.coded.tolist()  # type:list
        coded.extend(MappingEncoder.coding(self.coder, self.states, records))
        self.coded = array(coded, dtype=int)

    def mapping(self, records: list):
        """
        添加新的映射关系
        :param records:
        :return:
        """
        self.states = records
