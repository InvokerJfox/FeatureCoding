from encode.example.record import CommonRecords
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.list.EncodeList import EncodeList
from encode.list.UniqueList import encode_to_unique

vertex_interpreter = CountingInterpreter(encode_dimensions=CommonRecords.vertex_encodes,
                                         feature_dimensions=CommonRecords.vertex_features,
                                         counting_dimension=CommonRecords.vertex_counting)
goods1 = EncodeList(vertex_interpreter, CommonRecords.goods1)
goods2 = EncodeList(vertex_interpreter, CommonRecords.goods2)
print(goods1.records)
print(goods2.records)
goods1 = encode_to_unique(goods1)
goods2 = encode_to_unique(goods2)


print(goods1.records)
print(goods2.records)

# vertex_encoder = OneHotEncoder(vertex_compressor)
# vertex_encoder.coding(CommonRecords.goods1)
# vertex_encoder.coding(CommonRecords.goods2)

# print("coder_records=%s" % vertex_encoder.coder.records.tolist())
# print("coder_uniques=%s" % vertex_encoder.coder.uniques)
# print("coder_protects=%s" % vertex_encoder.coder.protects)

# vertex_encoder.encoding(CommonRecords.goods2)
# vertex_encoder.encoding(CommonRecords.goods1)
# print("coded_records=%s" % vertex_encoder.coded.records.tolist())
# print("coded_uniques=%s" % vertex_encoder.coded.uniques)
# print("coded_protect_uniques=%s" % vertex_encoder.coded.protect_uniques)
#
# edge_interpreter = MappingInterpreter(start_dimension=CommonRecords.edge_start,
#                                       target_dimension=CommonRecords.edge_target,
#                                       encode_dimensions=CommonRecords.edge_encodes,
#                                       feature_dimensions=CommonRecords.edge_features)
# # edge_compressor = CountingCompressor(edge_interpreter)
# edge_encoder = MappingEncoder(edge_compressor)
#
# print("records=%s" % vertex_encoder.coding.records.tolist())
# print("uniques=%s" % vertex_encoder.coding.uniques)
# print("protects=%s" % vertex_encoder.coding.protects)

# edge_compressed.extend(CommonRecords.jobs1)
# edge_compressed.extend(CommonRecords.jobs1)
# print("edge_compressed_data=%s" % edge_compressed.data)
#
# edge_coder = MappingEncoder.coding(edge_compressed, interpreter=edge_interpreter)

# print("vertices=%s" % qualityGraphCoder.vertices)
# print("vertex_descriptions=%s" % qualityGraphCoder.vertex_descriptions)
# print("vertex_indexes=%s" % qualityGraphCoder.vertex_indexes)
# print("edges=%s" % qualityGraphCoder.edges)
# print("edges_descriptions=%s" % qualityGraphCoder.edge_descriptions)
#
# qualityGraphData = RouteData(qualityGraphCoder)
# qualityGraphData.append_vertices(CommonRecords.jobs)
# qualityGraphData.append_edges(CommonRecords.jobs)
#
# print("coded=%s" % qualityGraphData.coded)
# print("coded description=%s" % qualityGraphData.description)
