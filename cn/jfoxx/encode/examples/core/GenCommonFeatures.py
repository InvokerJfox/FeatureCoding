from encode.example.data import CommonRecords
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.list.CountingList import CountingList
from encode.projector.OneHotProjector import OneHotProjector

from cn.jfoxx.encode.core.list.ProjectedList import ProjectedList

good_interpreter = CountingInterpreter(dimensions=CommonRecords.vertex_projects,
                                       encode_dimensions=CommonRecords.vertex_encodes,
                                       feature_dimensions=CommonRecords.vertex_features,
                                       counting_dimension=CommonRecords.vertex_counting)

goods = CountingList(good_interpreter)
goods.extend(CommonRecords.goods1)
goods.extend(CommonRecords.goods2)
good_projector = OneHotProjector(good_interpreter)
good_projector.feed(CommonRecords.goods1)
good_projector.feed(CommonRecords.goods2)
print("good_projector_records=%s" % good_projector.records)
print("good_projector_projects=%s" % good_projector.projects)
print("good_projector_project_indexes=%s" % good_projector.project_indexes)
good_projected = ProjectedList(good_projector)
good_projected.extend(CommonRecords.goods2)
good_projected.extend(CommonRecords.goods1)
print("good_projector_records=%s" % good_projected.records)
print("good_projector_protected=%s" % good_projected.protected)

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
