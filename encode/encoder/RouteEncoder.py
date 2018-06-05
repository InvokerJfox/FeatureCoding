from encode.decoding.RouteCoding import MappingCoder
from encode.list.CountingCompressor import CountingCompressor
from numpy import array

from encode.encoded.ProjectEncoded import OneHotCoded
from encode.encoded.RouteEncoded import MappingCoded
from encode.encoder.DimensionEncoder import DimensionCode
from encode.interpreter.CountingInterpreter import CountingInterpreter


class MappingEncoder(IEncoder):
    """
       对数据进行映射型one-hot编码
        1.首先将所有状态基于压缩器进行唯一编码(onehotid)
        2.基于这些状态的唯一编码，建立连接关系编码(MappingCoder)并生成连接结果(MappingCoded)

    """

    def __init__(self, compressor: CountingCompressor, vertices: OneHotCoded):
        """

        :param compressor:
        :param vertices:
        """
        super().__init__()
        # 初始化空的编码器和编码结果
        self.coding = MappingCoder(compressor)
        self.coded = MappingCoded(self.coding, vertices)

    def coding(self, records: list) -> MappingCoder:
        """
        通过特征生成一个映射型编码器
        :param records: 增量编码记录(与原数据不相关)
        :return:
        """
        # 读取编码器
        coding = self.coding
        # 读取压缩器
        compressor = coding.compressor
        # 读取解释器
        interpreter = coding.compressor.interpreter

        # 将数据分为起始/目标态进行解析,生成onehot码
        # 获取起始/目标/onehot维度
        start_dimension = interpreter.start_dimension
        target_dimension = interpreter.target_dimension
        onehot_dimension = interpreter.onehot_dimension
        # 获取编码维度,生成解释器
        encode_dimension = interpreter.encode_dimensions
        encode_interpreter = CountingInterpreter(encode_dimension)

        # onehot累积值

        # 遍历所有数据
        for record in records:  # type:dict
            # 获取起始/目标维度并进行编码
            start = record[start_dimension]  # type:dict

            encodes = encode_interpreter.encodes(interpreter.encodes(start))  # type:dict
            s = DimensionCode.unique(encodes)

            # 添加唯一索引
            onehot_dimension = coding.onehot_dimension
            new_codes = map(lambda x: x[onehot_dimension], records)
            coding.codes.extend(new_codes)

            # 全量压缩
            older = coding.records.tolist()
            older.extend(records)
            compressed = compressor.compress(older)
            # 存储
            coding.records = compressed

            # 获取原编码结果
            uniques = coding.uniques
            # 新旧编码长度不等则新增编码/维度码,对增量(所处的新数据)进行编码
            if len(uniques) != len(compressed.uniques):
                pass

            # 重置多维反射索引
            coding.code_indexes = dict(zip(coding.codes, range(len(coding.codes))))

            # 追加记录
            coding.descriptions.extend(records)

            return coding

            # 追加记录
            coding.descriptions.extend(records)
            # 获取编码维度
            start_key = coding.start_key
            target_key = coding.target_key
            # 取特征值:key为start与target的合并，value为start/target分别值
            codes = coding.codes.tolist()  # type:list
            # 每个记录
            for value in records:  # type:dict
                start = str(value[start_key])
                target = str(value[target_key])
                # 编码格式:start+v(start)+target+v(target)
                code = start_key + start + target_key + target
                codes.extend([code])

            # 更新
            coding.codes = array(codes)
            return coding

    def encoding(coding: list, state: list, mapping: list) -> list:
        """
        基于状态及映射关系进行编码效验并返回编码结果
        :param coding:
        :param state:
        :param mapping:list[dict]
        :return:
        """
        codes = coding.codes
        # 编码维度
        start_key = coding.start_key
        target_key = coding.target_key
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
        coded.extend(MappingEncoding.coding(self.coding, self.states, records))
        self.coded = array(coded, dtype=int)

    def mapping(self, records: list):
        """
        添加新的映射关系
        :param records:
        :return:
        """
        self.states = records
