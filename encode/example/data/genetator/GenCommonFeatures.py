from encode.compressor.CountingCompressor import CountingCompressor
from encode.encoder.OneHotEncoder import OneHotEncoder
from encode.example.data.record import CommonRecords
from encode.interpreter.CountingInterpreter import CountingInterpreter
from encode.list.CountingList import CountingList

interpreter = CountingInterpreter(CommonRecords.encodes, feature_dimensions=CommonRecords.features,
                                  counting_dimensions=CommonRecords.countings)
compressor = CountingCompressor(interpreter)
compressed = CountingList(compressor)
compressed.extend(CommonRecords.goods1)
compressed.extend(CommonRecords.goods2)

qualitySimpleCoder = OneHotEncoder.coder(compressed)
print("protects=%s" % qualitySimpleCoder.protects)
print("protect_indexes=%s" % qualitySimpleCoder.protect_indexes)
print("codes=%s" % qualitySimpleCoder.codes)
print("code_indexes=%s" % qualitySimpleCoder.code_indexes)
print("descriptions_data=%s" % qualitySimpleCoder.descriptions.data)

qualityCoded = OneHotEncoder.coding(compressed, qualitySimpleCoder)
print("coded=%s" % qualityCoded.coded)
print("coded_indexes=%s" % qualityCoded.coded_indexes)
print("descriptions_data=%s" % qualityCoded.descriptions.data)

# qualityInterpreter = RouteInterpreter(vertex_state_code_keys=["quality"], edge_start_key="from", edge_target_key="to")
# qualityGraphCoder = RouteEncoder.coder(CommonRecords.goods, interpreter=qualityInterpreter)
#
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
