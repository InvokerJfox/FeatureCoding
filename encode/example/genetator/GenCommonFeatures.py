from encode.compressor.CountingCompressor import CountingCompressor
from encode.encoder.MappingEncoder import MappingEncoder
from encode.encoder.OneHotEncoder import OneHotEncoder
from encode.example.record import CommonRecords
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.interpreter.MappingInterpreter import MappingInterpreter
from encode.list.CountingList import CountingList

vertex_interpreter = CountingInterpreter(CommonRecords.vertex_encodes,
                                         feature_dimensions=CommonRecords.vertex_features,
                                         counting_dimensions=CommonRecords.vertex_countings)
vertex_compressor = CountingCompressor(vertex_interpreter)

vertex_encoder = OneHotEncoder(vertex_compressor)
vertex_encoder.coding(CommonRecords.goods1)
vertex_encoder.coding(CommonRecords.goods2)

print("records=%s" % vertex_encoder.coder.records.tolist())
print("uniques=%s" % vertex_encoder.coder.uniques)
print("protects=%s" % vertex_encoder.coder.protects)

vertex_encoder.encoding(CommonRecords.goods2)
vertex_encoder.encoding(CommonRecords.goods1)
print("records=%s" % vertex_encoder.coded.records.tolist())
print("uniques=%s" % vertex_encoder.coded.uniques)
print("protect_uniques=%s" % vertex_encoder.coded.protect_uniques)

# edge_interpreter = MappingInterpreter(start_dimension=CommonRecords.edge_start,
#                                       target_dimension=CommonRecords.edge_target,
#                                       encode_dimensions=CommonRecords.edge_encodes,
#                                       state_default=CommonRecords.state_default,
#                                       feature_dimensions=CommonRecords.edge_features,
#                                       counting_dimensions=CommonRecords.edge_countings)
# edge_compressor = CountingCompressor(edge_interpreter)
# edge_encoder = MappingEncoder(edge_compressor)
# edge_compressed.extend(CommonRecords.jobs1)
# edge_compressed.extend(CommonRecords.jobs1)
# print("edge_compressed_data=%s" % edge_compressed.data)
#
# edge_coder = MappingEncoder.coder(edge_compressed, interpreter=edge_interpreter)

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
