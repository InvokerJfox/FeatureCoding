from numpy import array

from encode.encoder.CountingEncoder import OneHotEncoder
from encode.projector.DimensionProjector import DimensionProjector


class ProjectEncoder(OneHotEncoder):
    """
        具有编码维度投影至向量的编码器
    """

    def __init__(self, projector=DimensionProjector):
        """

        :param projector:
        """
        # 初始化空的编码器和编码结果
        super().__init__()
        self.project = projector

    def coding(self, records: list):
        """
        增量编译数据，生成编码结果
        :param records: 增量编码记录(与原数据不相关)
        :return:
        """
        # 读取编码器
        coding = self.coding
        # 读取压缩器
        compressor = self.compressor

        # 全量压缩
        # TODO 状态数据除了增量数据，也有状态移除问题需要处理
        older = coding.records.tolist()
        older.extend(records)
        compressed = compressor.compress(older)
        # 存储
        coding.records = compressed

        # 获取原编码结果
        uniques = coding.uniques
        # 新旧编码长度不等则新增编码/维度码,对增量(所处的新数据)进行编码
        if len(uniques) != len(compressed.uniques):
            # TODO 增量最好在压缩过程中生成(新增非必要增量参数),但当前投影有包含去重处理
            # 新数据进行编码
            increments = compressor.compress(records).tolist()
            # 获取多维投影仪
            projector = coding.projector  # type:DimensionProjector
            # 获取编码维度
            encode_dimensions = coding.compressor.interpreter.encode_dimensions  # type:list
            # 获取原多维映射码
            protects = coding.protects  # type:dict
            # 对新数据进行多维编码 & 更新
            projector.project(increments, encode_dimensions, protects)
            # 重置多维反射索引
            coding.protect_indexes = dict(zip(protects, range(len(protects))))

            # 更新唯一编码结果
            coding.uniques = compressed.uniques
            # 重置多维反射索引
            coding.unique_indexes = dict(zip(coding.uniques, range(len(coding.uniques))))

    def encoding(self, records: list):
        """
        数据增量生成独热编码、投影码;并保存在Coded对象中
        :param records:增量编码记录(与原数据不相关)
        :return:
        """
        # 获取编码器
        coding = self.coding
        # 读取压缩器
        compressor = coding.compressor
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
            projector = coding.projector
            # 获取编码维度
            encode_dimensions = coding.compressor.interpreter.encode_dimensions  # type:list
            # 获取多维编码
            protects = coding.protects  # type:dict
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
