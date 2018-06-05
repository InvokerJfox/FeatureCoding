import numpy as np

from encode.example.record import CommonRecords
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.interpreter.DefaultInterpreter import DefaultInterpreter
from encode.list.CountingList import CountingList
from encode.mapper.projector.OneHotProjector import OneHotProjector

good_interpreter = CountingInterpreter(encode_dimensions=CommonRecords.vertex_encodes,
                                       feature_dimensions=CommonRecords.vertex_features,
                                       counting_dimension=CommonRecords.vertex_counting)
goods = CountingList(good_interpreter)
goods.extend(CommonRecords.goods1)
goods.extend(CommonRecords.goods2)

print("goods_records=%s" % goods.records)

project_interpreter = DefaultInterpreter(dimensions=CommonRecords.vertex_projects)
good_projector = OneHotProjector(project_interpreter)
good_projector.feed(goods.records)
good_projected = good_projector.project(CommonRecords.goods1)
good_projected.extend(good_projector.project(CommonRecords.goods2))
print("good_projector=%s" % good_projector.projects)
print("good_projected=%s" % good_projected)
print(np.array(good_projected))


# vertex_encoder.coding(CommonRecords.goods1)
# vertex_encoder.coding(CommonRecords.goods2)


# vertex_encoder.encoding(CommonRecords.goods2)
# vertex_encoder.encoding(CommonRecords.goods1)
# print("coded_records=%s" % vertex_encoder.encoded.records.tolist())
# print("coded_uniques=%s" % vertex_encoder.encoded.uniques)
# print("coded_protect_uniques=%s" % vertex_encoder.encoded.protect_uniques)
#
# edge_interpreter = MappingInterpreter(start_dimension=CommonRecords.edge_start,
#                                       target_dimension=CommonRecords.edge_target,
#                                       encode_dimensions=CommonRecords.edge_encodes,
#                                       feature_dimensions=CommonRecords.edge_features)
# # edge_compressor = CountingCompressor(edge_interpreter)
# edge_encoder = MappingEncoder(edge_compressor)
#
# print("records=%s" % vertex_encoder.decoding.records.tolist())
# print("uniques=%s" % vertex_encoder.decoding.uniques)
# print("protects=%s" % vertex_encoder.decoding.protects)

# edge_compressed.extend(CommonRecords.jobs1)
# edge_compressed.extend(CommonRecords.jobs1)
# print("edge_compressed_data=%s" % edge_compressed.data)
#
# edge_coder = MappingEncoder.decoding(edge_compressed, interpreter=edge_interpreter)

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
# print("encoded=%s" % qualityGraphData.encoded)
# print("encoded description=%s" % qualityGraphData.description)
