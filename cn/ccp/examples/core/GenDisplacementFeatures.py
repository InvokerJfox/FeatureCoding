from hashlib import md5

from encode.example.entity.displacement.entry.Area import Area
from encode.example.entity.displacement.entry.Coordinate import Coordinate
from encode.example.entity.displacement.entry.Path import Path
from encode.example.entity.displacement.entry.PathNode import PathNode

from cn.ccp.encode.examples.entity.displacement.entry.Map import Map

'''
    1张 世界地图 && 2张仓库地图(1层,2层)
'''
world = Map(md5('世界地图'), '世界地图')
warehouse1 = Map(md5('仓库1层'), '仓库1层')
warehouse2 = Map(md5('仓库2层'), '仓库2层')

'''
    1张 世界地图 with 10000x10000 边界坐标点,其含 5个 区域 x 1个 边界坐标点 && 16条路径 && 20个 位置坐标点
'''
world_boundary_area = Area(md5(), '世界地图边界', 0, 1000,
                           boundary_coordinate=[Coordinate(0, 0), Coordinate(0, 10000),
                                                Coordinate(10000, 10000), Coordinate(10000, 0)])

world_areas = [Area(md5('仓库货运站'), '仓库货运站', 0, 100, boundary_coordinate=[Coordinate(1000, 1000)]),
               Area(md5('华南中转站'), '华南中转站', 0, 100, boundary_coordinate=[Coordinate(1000, 5000)]),
               Area(md5('华东中转站'), '华东中转站', 0, 100, boundary_coordinate=[Coordinate(1500, 1000)]),
               Area(md5('华北中转站'), '华北中转站', 0, 100, boundary_coordinate=[Coordinate(1000, 1500)]),
               Area(md5('华西中转站'), '华西中转站', 0, 100, boundary_coordinate=[Coordinate(500, 1000)])]

world_paths_nodes = [PathNode('仓库货运站路径结点', [Coordinate(1000, 1000)]),
                     PathNode('华南中转站路径结点', [Coordinate(1000, 5000)]),
                     PathNode('华东中转站路径结点', [Coordinate(1500, 1000)]),
                     PathNode('华北中转站路径结点', [Coordinate(1000, 1500)]),
                     PathNode('华西中转站路径结点', [Coordinate(500, 1000)])]

world_paths = [Path('仓库→华南', world_paths_nodes[0], world_paths_nodes[1], 500),
               Path('仓库→华东', world_paths_nodes[0], world_paths_nodes[2], 500),
               Path('仓库→华北', world_paths_nodes[0], world_paths_nodes[3], 500),
               Path('仓库→华西', world_paths_nodes[0], world_paths_nodes[4], 500),
               Path('华南→华西', world_paths_nodes[1], world_paths_nodes[4], 500),
               Path('华南→仓库', world_paths_nodes[1], world_paths_nodes[0], 500),
               Path('华南→华东', world_paths_nodes[1], world_paths_nodes[2], 500),
               Path('华东→华北', world_paths_nodes[2], world_paths_nodes[3], 500),
               Path('华东→仓库', world_paths_nodes[2], world_paths_nodes[0], 500),
               Path('华东→华南', world_paths_nodes[2], world_paths_nodes[1], 500),
               Path('华北→华西', world_paths_nodes[3], world_paths_nodes[4], 500),
               Path('华北→仓库', world_paths_nodes[3], world_paths_nodes[0], 500),
               Path('华北→华东', world_paths_nodes[3], world_paths_nodes[3], 500),
               Path('华西→华北', world_paths_nodes[4], world_paths_nodes[3], 500),
               Path('华西→仓库', world_paths_nodes[4], world_paths_nodes[0], 500),
               Path('华西→华南', world_paths_nodes[4], world_paths_nodes[1], 500)]

world.boundary_area = world_boundary_area
world.areas = world_areas
world.path_node = world_paths_nodes

'''
    1张 仓库1层地图 with 200x400 边界坐标点,其含 3个 区域 x 4个 边界坐标点 && 16x2条'主要'路径 && ??个 位置坐标点
'''
warehouse1_boundary_area = Area(md5('仓库1层地图边界'), '仓库1层地图边界', 0, 100, boundary_coordinate=[
    Coordinate(0, 0), Coordinate(0, 400), Coordinate(200, 400), Coordinate(200, 0)])

warehouse1_areas = [Area(md5('仓库1层存货区区域'), '仓库1层存货区区域', 0, 100, boundary_coordinate=[
    Coordinate(0, int(400 / 3 * 2)), Coordinate(0, int(400)), Coordinate(200, int(400 / 3 * 2)),
    Coordinate(200, int(400))]),
                    Area(md5('仓库1层作业区区域'), '仓库1层作业区区域', 0, 100,
                         boundary_coordinate=[Coordinate(int(200 / 3), int(400 / 3)),
                                              Coordinate(int(200 / 3), int(400 / 3 * 1.8)),
                                              Coordinate(int(200 / 3 * 2), int(400 / 3 * 1.8)),
                                              Coordinate(int(200 / 3 * 2), int(400 / 3))]),
                    Area(md5('仓库1层交接区区域'), '仓库1层交接区区域', 0, 100,
                         boundary_coordinate=[Coordinate(int(200 / 3), int(0)),
                                              Coordinate(int(200 / 3), int(400 / 3 * 0.8)),
                                              Coordinate(int(200 / 3 * 2), int(400 / 3 * 0.8)),
                                              Coordinate(int(200 / 3 * 2), int(0))])]
# 第一行 7关键结点
# 第二行 2关键结点
# 第三行 9关键结点
# 第四行 空
# 第五行 8关键结点
# 第六行 1关键节点
warehouse1_paths_nodes = [
    Coordinate(int(200 / 19 * 2), int(400 / 6 * 6)), Coordinate(int(200 / 19 * 4), int(400 / 6 * 6)),
    Coordinate(int(200 / 19 * 6), int(400 / 6 * 6)), Coordinate(int(200 / 19 * 8), int(400 / 6 * 6)),
    Coordinate(int(200 / 19 * 10), int(400 / 6 * 6)), Coordinate(int(200 / 19 * 12), int(400 / 6 * 6)),
    Coordinate(int(200 / 19 * 14), int(400 / 6 * 6)),
    Coordinate(int(200 / 19 * 4), int(400 / 6 * 5)), Coordinate(int(200 / 19 * 12), int(400 / 6 * 5)),
    Coordinate(int(200 / 19 * 2), int(400 / 6 * 4)), Coordinate(int(200 / 19 * 5), int(400 / 6 * 4)),
    Coordinate(int(200 / 19 * 6), int(400 / 6 * 4)), Coordinate(int(200 / 19 * 7), int(400 / 6 * 4)),
    Coordinate(int(200 / 19 * 8), int(400 / 6 * 4)), Coordinate(int(200 / 19 * 9), int(400 / 6 * 4)),
    Coordinate(int(200 / 19 * 10), int(400 / 6 * 4)), Coordinate(int(200 / 19 * 11), int(400 / 6 * 4)),
    Coordinate(int(200 / 19 * 14), int(400 / 6 * 4)),
    Coordinate(int(200 / 19 * 2), int(400 / 6 * 2)), Coordinate(int(200 / 19 * 4), int(400 / 6 * 2)),
    Coordinate(int(200 / 19 * 5), int(400 / 6 * 2)), Coordinate(int(200 / 19 * 7), int(400 / 6 * 2)),
    Coordinate(int(200 / 19 * 9), int(400 / 6 * 2)), Coordinate(int(200 / 19 * 11), int(400 / 6 * 2)),
    Coordinate(int(200 / 19 * 12), int(400 / 6 * 2)), Coordinate(int(200 / 19 * 14), int(400 / 6 * 2)),
    Coordinate(int(200 / 19 * 8), int(400 / 6 * 1))]

# 路线 2(双向) x (1+1+4+0+4+9+1)
warehouse1_paths = [Path('2,6→14,6', warehouse1_paths_nodes[0], warehouse1_paths_nodes[6], (14 - 2) * (200 / 17)),
                    Path('4,5→12,5', warehouse1_paths_nodes[7], warehouse1_paths_nodes[8], (12 - 4) * (200 / 17)),
                    Path('2,4→14,4', warehouse1_paths_nodes[9], warehouse1_paths_nodes[17], (14 - 2) * (200 / 17)),
                    Path('6,6→6,4', warehouse1_paths_nodes[2], warehouse1_paths_nodes[11], (6 - 4) * (400 / 6)),
                    Path('8,6→8,4', warehouse1_paths_nodes[3], warehouse1_paths_nodes[13], (6 - 4) * (400 / 6)),
                    Path('10,6→10,4', warehouse1_paths_nodes[4], warehouse1_paths_nodes[15], (6 - 4) * (400 / 6)),
                    Path('2,2→14,2', warehouse1_paths_nodes[18], warehouse1_paths_nodes[25], (14 - 2) * (200 / 17)),
                    Path('2,6→2,2', warehouse1_paths_nodes[0], warehouse1_paths_nodes[18], (6 - 2) * (400 / 6)),
                    Path('4,6→4,2', warehouse1_paths_nodes[1], warehouse1_paths_nodes[19], (6 - 2) * (400 / 6)),
                    Path('12,6→12,2', warehouse1_paths_nodes[5], warehouse1_paths_nodes[24], (6 - 2) * (400 / 6)),
                    Path('14,6→14,2', warehouse1_paths_nodes[6], warehouse1_paths_nodes[25], (6 - 2) * (400 / 6)),
                    Path('5,4→5,2', warehouse1_paths_nodes[10], warehouse1_paths_nodes[20], (4 - 2) * (400 / 6)),
                    Path('7,4→7,2', warehouse1_paths_nodes[12], warehouse1_paths_nodes[21], (4 - 2) * (400 / 6)),
                    Path('9,4→9,2', warehouse1_paths_nodes[14], warehouse1_paths_nodes[22], (4 - 2) * (400 / 6)),
                    Path('11,4→11,2', warehouse1_paths_nodes[16], warehouse1_paths_nodes[23], (4 - 2) * (400 / 6)),
                    Path('8,2→8,1', warehouse1_paths_nodes[21], warehouse1_paths_nodes[26], (2 - 1) * (400 / 6)),

                    Path('2,6→14,6', warehouse1_paths_nodes[6], warehouse1_paths_nodes[0], (14 - 2) * (200 / 17)),
                    Path('4,5→12,5', warehouse1_paths_nodes[8], warehouse1_paths_nodes[7], (12 - 4) * (200 / 17)),
                    Path('2,4→14,4', warehouse1_paths_nodes[17], warehouse1_paths_nodes[9], (14 - 2) * (200 / 17)),
                    Path('6,6→6,4', warehouse1_paths_nodes[11], warehouse1_paths_nodes[2], (6 - 4) * (400 / 6)),
                    Path('8,6→8,4', warehouse1_paths_nodes[13], warehouse1_paths_nodes[3], (6 - 4) * (400 / 6)),
                    Path('10,6→10,4', warehouse1_paths_nodes[15], warehouse1_paths_nodes[4], (6 - 4) * (400 / 6)),
                    Path('2,2→14,2', warehouse1_paths_nodes[25], warehouse1_paths_nodes[18], (14 - 2) * (200 / 17)),
                    Path('2,6→2,2', warehouse1_paths_nodes[18], warehouse1_paths_nodes[0], (6 - 2) * (400 / 6)),
                    Path('4,6→4,2', warehouse1_paths_nodes[19], warehouse1_paths_nodes[1], (6 - 2) * (400 / 6)),
                    Path('12,6→12,2', warehouse1_paths_nodes[24], warehouse1_paths_nodes[5], (6 - 2) * (400 / 6)),
                    Path('14,6→14,2', warehouse1_paths_nodes[25], warehouse1_paths_nodes[6], (6 - 2) * (400 / 6)),
                    Path('5,4→5,2', warehouse1_paths_nodes[20], warehouse1_paths_nodes[10], (4 - 2) * (400 / 6)),
                    Path('7,4→7,2', warehouse1_paths_nodes[21], warehouse1_paths_nodes[12], (4 - 2) * (400 / 6)),
                    Path('9,4→9,2', warehouse1_paths_nodes[22], warehouse1_paths_nodes[14], (4 - 2) * (400 / 6)),
                    Path('11,4→11,2', warehouse1_paths_nodes[23], warehouse1_paths_nodes[16], (4 - 2) * (400 / 6)),
                    Path('8,2→8,1', warehouse1_paths_nodes[26], warehouse1_paths_nodes[21], (2 - 1) * (400 / 6))]

warehouse1.boundary_area = warehouse1_boundary_area
warehouse1.areas = warehouse1_areas
warehouse1.path_node = warehouse1_paths_nodes

'''
    1张 仓库2层地图 with 600x100 边界坐标点,其含 1个 区域 x 4个 边界坐标点 && 16x2条'主要'路径 && ??个 位置坐标点
'''
warehouse2_boundary_area = Area(md5('仓库2层地图边界'), '仓库2层地图边界', 0, 100, boundary_coordinate=[
    Coordinate(0, 0), Coordinate(0, 100), Coordinate(600, 100), Coordinate(600, 0)])

warehouse2_areas = [Area(md5('仓库2层存货区区域'), '仓库2层存货区区域', 0, 100, boundary_coordinate=[
    Coordinate(0, int(100 / 6)), Coordinate(0, int(100)), Coordinate(600, int(100)),
    Coordinate(600, int(100 / 6))])]

# 第一行 13关键结点
# 第二行 2关键结点
# 第三行 12关键结点
# 第四行 1关键结点
warehouse2_paths_nodes = [
    Coordinate(int(600 / 12 * 0), int(100 / 4 * 4)), Coordinate(int(600 / 12 * 1), int(100 / 4 * 4)),
    Coordinate(int(600 / 12 * 2), int(100 / 4 * 4)), Coordinate(int(600 / 12 * 3), int(100 / 4 * 4)),
    Coordinate(int(600 / 12 * 4), int(100 / 4 * 4)), Coordinate(int(600 / 12 * 5), int(100 / 4 * 4)),
    Coordinate(int(600 / 12 * 6), int(100 / 4 * 4)), Coordinate(int(600 / 12 * 7), int(100 / 4 * 4)),
    Coordinate(int(600 / 12 * 8), int(100 / 4 * 4)), Coordinate(int(600 / 12 * 9), int(100 / 4 * 4)),
    Coordinate(int(600 / 12 * 10), int(100 / 4 * 4)), Coordinate(int(600 / 12 * 11), int(100 / 4 * 4)),
    Coordinate(int(600 / 12 * 12), int(100 / 4 * 4)),
    Coordinate(int(600 / 12 * 0), int(100 / 4 * 3)), Coordinate(int(600 / 12 * 12), int(100 / 4 * 3)),
    Coordinate(int(600 / 12 * 0), int(100 / 4 * 2)), Coordinate(int(600 / 12 * 1), int(100 / 4 * 2)),
    Coordinate(int(600 / 12 * 2), int(100 / 4 * 2)), Coordinate(int(600 / 12 * 3), int(100 / 4 * 2)),
    Coordinate(int(600 / 12 * 4), int(100 / 4 * 2)), Coordinate(int(600 / 12 * 5), int(100 / 4 * 2)),
    Coordinate(int(600 / 12 * 7), int(100 / 4 * 2)), Coordinate(int(600 / 12 * 8), int(100 / 4 * 2)),
    Coordinate(int(600 / 12 * 9), int(100 / 4 * 2)), Coordinate(int(600 / 12 * 10), int(100 / 4 * 2)),
    Coordinate(int(600 / 12 * 11), int(100 / 4 * 2)), Coordinate(int(600 / 12 * 12), int(100 / 4 * 2)),
    Coordinate(int(600 / 12 * 6), int(100 / 4 * 1))]

# 路线 2(双向) x (1+1+14)
warehouse2_paths = [Path('0,4→12,4', warehouse2_paths_nodes[0], warehouse2_paths_nodes[12], (12 - 0) * (600 / 12)),
                    Path('0,3→12,3', warehouse2_paths_nodes[13], warehouse2_paths_nodes[14], (12 - 0) * (600 / 12)),
                    Path('0,2→12,2', warehouse2_paths_nodes[15], warehouse2_paths_nodes[26], (12 - 0) * (600 / 12)),
                    Path('0,4→0,2', warehouse2_paths_nodes[0], warehouse2_paths_nodes[15], (4 - 2) * (100 / 4)),
                    Path('1,4→1,2', warehouse2_paths_nodes[1], warehouse2_paths_nodes[16], (4 - 2) * (100 / 4)),
                    Path('2,4→2,2', warehouse2_paths_nodes[2], warehouse2_paths_nodes[17], (4 - 2) * (100 / 4)),
                    Path('3,4→3,2', warehouse2_paths_nodes[3], warehouse2_paths_nodes[18], (4 - 2) * (100 / 4)),
                    Path('4,4→4,2', warehouse2_paths_nodes[4], warehouse2_paths_nodes[19], (4 - 2) * (100 / 4)),
                    Path('5,4→5,2', warehouse2_paths_nodes[5], warehouse2_paths_nodes[20], (4 - 2) * (100 / 4)),
                    Path('6,4→6,1', warehouse2_paths_nodes[6], warehouse2_paths_nodes[27], (4 - 1) * (100 / 4)),
                    Path('7,4→7,2', warehouse2_paths_nodes[7], warehouse2_paths_nodes[21], (4 - 2) * (100 / 4)),
                    Path('8,4→8,2', warehouse2_paths_nodes[8], warehouse2_paths_nodes[22], (4 - 2) * (100 / 4)),
                    Path('9,4→9,2', warehouse2_paths_nodes[9], warehouse2_paths_nodes[23], (4 - 2) * (100 / 4)),
                    Path('10,4→10,2', warehouse2_paths_nodes[10], warehouse2_paths_nodes[24], (4 - 2) * (100 / 4)),
                    Path('11,4→11,2', warehouse2_paths_nodes[11], warehouse2_paths_nodes[25], (4 - 2) * (100 / 4)),
                    Path('12,4→12,2', warehouse2_paths_nodes[12], warehouse2_paths_nodes[26], (4 - 2) * (100 / 4))]

warehouse2.boundary_area = warehouse2_boundary_area
warehouse2.areas = warehouse2_areas
warehouse2.path_node = warehouse2_paths_nodes

'''
    2条地图间路径 仓库地图1层(交接区)↔仓库地图2层(交接区)
    2条地图间路径 仓库地图1层(交接区)↔世界地图(地区)
'''
# map_to_map_path = [Path('1上2层')]

# print('>>>>>>world:')
# world.display()
# print('>>>>>>warehouse1:')
# warehouse1.display()
# print('>>>>>>warehouse2:')
# warehouse2.display()
print('>>>>>>warehouse2_paths:')
for item in warehouse2_paths:
    item.display()
