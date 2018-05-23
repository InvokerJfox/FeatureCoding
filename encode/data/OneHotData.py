from numpy import array

from encode.coder.OneHotCoder import OneHotCoder
from encode.data.Data import Data
from encode.encoder.OneHotEncoder import OneHotEncoder


class OneHotData(Data):
    """
    用于存储独热编码后的数据
    注:1.输入值不允许重复(不可重定义)
    2.不允许使用onehot字段，其被作为编码结果唯一码使用
    """

    def __init__(self, coder: OneHotCoder):
        """
        初始化一个编码结果存储单元
        :param coder:编码表
        """
        super().__init__()
        self.coder = coder  # 编码器
        self.descriptions = []  # 编码原数据及编码结果
        self.coded = array(())  # 编码后的数据:{编码后状态值}
        self.coded_indexes = {}  # 通过编码唯一码反射原数据/编码数据索引,编码值一

    def append(self, records: list):
        """
        添加新数据
        :param records:待新增数据
        :return:
        """
        # 新增数据
        self.descriptions.extend(records)
        # 新增编码结果
        coded = self.coded.tolist()  # type:list
        coded.extend(OneHotEncoder.coding(self.coder, records))
        self.coded = array(coded, dtype=int)

        # 重置反射索引
        onehots = map(lambda x: x[self.coder.onehot_ukid], records)
        self.coded_indexes = dict(zip(list(onehots), range(len(records))))

        # 若出现重复定义，索引数不等于数据量，则抛出异常
        if len(records) != len(self.coded_indexes):
            raise ValueError('input repeat records to coder')
