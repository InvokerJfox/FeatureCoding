from numpy import zeros
from numpy import array
from encode.coder.OneHotCoder import OneHotCoder
from encode.encoder.Encoder import Encoder


class OneHotEncoder(Encoder):
    """
        定义编码规模,对数据进行one-hot编码(0/1编码)
    """

    @staticmethod
    def coder(records: list, coder=None, code_dimensions=None) -> OneHotCoder:
        """
        通过特征生成一个简单的独热编码器,coder和code_dimensions至少一个不为空
        :param records: 编码的所有记录(含说明)
        :param coder: 编码器
        :param code_dimensions: 记录中编码的字段名
        :return:
        """
        # coder和code_dimensions其一不为空
        if coder is None:
            if code_dimensions is not None:
                coder = OneHotCoder(code_dimensions)
            else:
                raise ValueError("'coder' and 'code_dimensions' at least one is not empty")

        # 对所有数据进行编码
        # 获取编码维度
        code_dimensions = coder.dimensions
        # 获取原编码 & 原编码索引
        codes = coder.codes.tolist()  # type:list
        code_indexes = coder.code_indexes  # type:dict
        # 记录新编码反射索引
        start_index = len(code_indexes)
        # 访问每个新记录,当不存在时,添加该编码及反射索引
        for record_index in range(len(records)):
            record = records[record_index]  # type:dict
            for code_key in code_dimensions:  # type:str
                # 编码
                code = coder.combiner.combine([code_key, str(record[code_key])])
                # 判断是否存在/添加
                if code not in code_indexes:
                    codes.extend([code])
                    code_indexes[code] = start_index + record_index
        # 扩展新增至编码结果
        coder.codes = array(codes)

        # 重建倒索引
        coder.code_indexes = dict(zip(codes, range(len(codes))))
        # 追加输入记录(可能含重复的定义)
        coder.descriptions.extend(records)

        return coder

    @staticmethod
    def coding(coder: OneHotCoder, records: list) -> list:
        """
        将数据生成独热编码，并将其作为唯一标识(onehot字段)放入数据中
        :param coder:
        :param records:list[dict]
        :return:
        """
        # 已存在编码
        codes = coder.codes  # type:array
        # 编码维度
        code_dimensions = coder.dimensions

        # 规模
        codes_size = len(codes)
        data_size = len(records)

        # 编码结果
        coded = zeros((data_size, codes_size))
        # 遍历所有数据
        for record_index in range(data_size):
            record = records[record_index]  # type:dict
            onehot = []  # 独热唯一码
            # 选取所有要编码的字段
            # 依次对比编码对象,匹配成功则匹配下一个
            codes_index = 0
            for code_dimension in code_dimensions:
                # 编码:
                code = coder.combiner.combine([code_dimension, str(record[code_dimension])])
                onehot.append(code_dimension)
                onehot.append(str(record[code_dimension]))
                while codes_index < codes_size:
                    # 若值与编码匹配则标记，且不再查找下一编码
                    if code == codes[codes_index]:
                        coded[record_index, codes_index] = 1
                        break
                    codes_index += 1
            # 存储独热唯一码
            record[coder.onehot_ukid] = coder.combiner.combine(onehot)

        return coded.tolist()
