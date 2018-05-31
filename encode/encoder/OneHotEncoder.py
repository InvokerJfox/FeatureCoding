from numpy import array

from encode.coded.OneHotCoded import OneHotCoded
from encode.coder.OneHotCoder import OneHotCoder
from encode.compressor.CountingCompressor import CountingCompressor
from encode.encoder.IEncoder import IEncoder
from encode.projector.DimensionProjector import DimensionProjector


class OneHotEncoder(IEncoder):
    """
        对数据进行one-hot编码(0/1编码)
    """

    def __init__(self, compressor: CountingCompressor, projector=DimensionProjector):
        """

        :param compressor:
        :param projector:
        """
        # 初始化空的编码器和编码结果
        self.coder = OneHotCoder(compressor, projector)
        self.coded = OneHotCoded(self.coder)

    def coding(self, records: list):
        """
        增量编译数据，生成编码结果
        :param records: 增量编码记录(与原数据不相关)
        :return:
        """
        # 读取编码器
        coder = self.coder
        # 读取压缩器
        compressor = coder.compressor

        # 全量压缩
        # TODO 状态数据除了增量数据，也有状态移除问题需要处理
        older = coder.records.tolist()
        older.extend(records)
        compressed = compressor.compress(older)
        # 存储
        coder.records = compressed

        # 获取原编码结果
        uniques = coder.uniques
        # 新旧编码长度不等则新增编码/维度码,对增量(所处的新数据)进行编码
        if len(uniques) != len(compressed.uniques):
            # TODO 增量最好在压缩过程中生成(新增非必要增量参数),但当前投影有包含去重处理
            # 新数据进行编码
            increments = compressor.compress(records).tolist()
            # 获取多维投影仪
            projector = coder.projector  # type:DimensionProjector
            # 获取编码维度
            encode_dimensions = coder.compressor.interpreter.encode_dimensions  # type:list
            # 获取原多维映射码
            protects = coder.protects  # type:dict
            # 对新数据进行多维编码 & 更新
            projector.project(increments, encode_dimensions, protects)
            # 重置多维反射索引
            coder.protect_indexes = dict(zip(protects, range(len(protects))))

            # 更新唯一编码结果
            coder.uniques = compressed.uniques
            # 重置多维反射索引
            coder.unique_indexes = dict(zip(coder.uniques, range(len(coder.uniques))))

    def encoding(self, records: list):
        """
        数据增量生成独热编码、投影码;并保存在Coded对象中
        :param records:增量编码记录(与原数据不相关)
        :return:
        """
        # 获取编码器
        coder = self.coder
        # 读取压缩器
        compressor = coder.compressor
        # 获取解释器
        interpreter = compressor.interpreter
        # 获取已编码结果
        coded = self.coded

        # 全量压缩
        older = coded.records.tolist()
        older.extend(records)
        compressed = compressor.compress(older)
        # 存储
        coded.records = compressed

        # 获取原编码结果
        uniques = coded.uniques
        # 新旧数据长度不等则对新"投影编码",对增量(验证新数据是否存在于旧数据中)进行编码
        if len(uniques) != len(compressed.uniques):
            # 获取多维投影仪
            projector = coder.projector
            # 获取编码维度
            encode_dimensions = coder.compressor.interpreter.encode_dimensions  # type:list
            # 获取多维编码
            protects = coder.protects  # type:dict
            # 获取已进行编码的数据
            protect_coded = coded.protect_uniques.tolist()  # type:list

            # 新数据进行编码
            increments = compressor.compress(records).tolist()
            for record in increments:
                # 若该数据不在已投影数据中
                if interpreter.onehot(record) not in coded.uniques:
                    # 对该新数据进行多维编码
                    projector.projecting([record], encode_dimensions, protects, protect_coded)

            # 存储编码结果
            coded.protect_uniques = array(protect_coded, dtype=int)

            # 更新唯一编码结果
            coded.uniques = compressed.uniques
            # 重置多维反射索引
            coded.unique_indexes = dict(zip(coded.uniques, range(len(coded.uniques))))

            self.coded = coded
