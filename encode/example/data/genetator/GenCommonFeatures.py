from encode.data.SimpleOneHotData import SimpleOneHotData
from encode.encoder.SimpleOneHotEncoder import SimpleOneHotEncoder

from encode.example.data.record import CommonRecords

qualityCoder = SimpleOneHotEncoder.register("quality_common_code", CommonRecords.qualitys, "defined")
print(qualityCoder.codes)
print(qualityCoder.description)

qualityData = SimpleOneHotData(qualityCoder, CommonRecords.goods, 'quality')
print(qualityData.data)
print(qualityData.description)
