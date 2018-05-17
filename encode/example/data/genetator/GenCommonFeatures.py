from encode.encoder.SimpleOneHotEncoder import SimpleOneHotEncoder

from encode.example.data.record import CommonRecords

qualityEncoder = SimpleOneHotEncoder("quality_common_code", CommonRecords.qualitys)
print(qualityEncoder.dimensions())

qualityEncoder.append(CommonRecords.data, 'quality')
print(qualityEncoder.code_data)
