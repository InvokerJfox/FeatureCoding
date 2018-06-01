from encode.coded.UniqueCoded import OneHotCoded
from encode.coding.UniqueCoding import OneHotCoding
from encode.encoder.IEncoder import IEncoder
from encode.list.UniqueList import OneHotList


class CountingEncoder(IEncoder):
    """
    计数编码器
    """
    @staticmethod
    def learn(coding: OneHotCoding, records: OneHotList):
        pass

    @staticmethod
    def forget(coding: OneHotCoding, indexes: list):
        pass

    @staticmethod
    def encode(coded: OneHotCoded, coding: OneHotCoding, records: OneHotList):
        """
        数据增量生成独热编码、投影码;并保存在Coded对象中
        :param coded: 编码结果
        :param coding:译码表
        :param records:增量编码记录(与原数据不相关)
        :return:
        """
        # 读取压缩器
        compressor = coding.compressor
        # 获取解释器
        interpreter = compressor.interpreter

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

    @staticmethod
    def remove(coded: OneHotCoded, indexes: list):
        pass
