from encode.data.MappingOneHotData import MappingOneHotData
from encode.data.SimpleOneHotData import SimpleOneHotData
from encode.encoder.MappingOntHotCoder import MappingOneHotEncoder
from encode.encoder.SimpleOneHotEncoder import SimpleOneHotEncoder
from encode.example.data.record import CommonRecords

# qualitySimpleCoder = SimpleOneHotEncoder.register("quality_common_code", CommonRecords.define_quality, "defined")
# print(qualitySimpleCoder.codes)
# print(qualitySimpleCoder.description)
#
# qualityData = SimpleOneHotData(qualitySimpleCoder)
# qualityData.append(CommonRecords.goods, 'quality')
# print(qualityData.data)
# print(qualityData.description)

qualityMappingCoder = MappingOneHotEncoder.register("quality_mapping_code", CommonRecords.define_operations,
                                                    start_key="from", target_key="to")
print("codes:%s" % qualityMappingCoder.codes)
print("codes description:%s" % qualityMappingCoder.description)

jobsData = MappingOneHotData(qualityMappingCoder)
jobsData.append(CommonRecords.jobs, start_key="from", target_key="to")

print("data:%s" % jobsData.data)
print("data description:%s" % jobsData.description)
