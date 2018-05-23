from encode.compress.Compressor import Compressor


class CounterCompressor(Compressor):
    @staticmethod
    def compress(records: list, unique_dimensions: list, counting_dimensions=None) -> list:
        """
        将原数据(records)按指定维度(unique_dimensions)进行相同值合并,合并时仅保留统计维度(counting_dimensions),并舍弃其他维度
        :param records: list[dict]
        :param unique_dimensions:
        :param counting_dimensions:
        :return:
        """
        if counting_dimensions is None:
            counting_dimensions = []

        # 取unique_dimensions及其值生成唯一码(dict),将相同值进行映射同时统计维度
        results = {}
        # 遍历所有数据
        for record in records:  # type:dict
            # 取维度&值生成唯一码
            code = ""
            for unique in unique_dimensions:
                code += unique + record[unique]

            # 若存在该记录则更新
            if code not in results:
                value = {}
                # 取特征值
                for unique in unique_dimensions:
                    value[unique] = record[unique]

                # 取统计维度值
                for counting in counting_dimensions:
                    value[counting] = record[counting]

                results[code] = value
            else:
                value = results[code]
                # 累加统计值
                for counting in counting_dimensions:
                    value[counting] += record[counting]

        return list(results.values())
