# 路由求解测试数据
# 状态编码维度
vertex_encodes = ["quality"]
# 状态特征维度
vertex_features = []
# 状态统计维度
vertex_countings = ["qty"]
# 映射连接起始维度
edge_start = "from"
# 映射连接目标维度
edge_target = "to"
# 映射中状态编码维度
edge_encodes = ["quality"]
# 映射中状态编码维度默认值
state_default = {"quality": -9999}
# 映射特征维度
edge_features = []
# 映射统计维度
edge_countings = []

# 消费物数据(作为状态/点):编码前(预处理/压缩)必须确定状态唯一性
goods1 = [{"id": 20000000000000001, "quality": "未知品质", "qty": 10},
          {"id": 20000000000000002, "quality": "未知品质", "qty": 30},
          {"id": 20000000000000003, "quality": "良品", "qty": 100},
          {"id": 20000000000000004, "quality": "未知品质", "qty": 10},
          {"id": 20000000000000005, "quality": "次品", "qty": 200},
          {"id": 20000000000000006, "quality": "良品", "qty": 10}]

goods2 = [{"id": 20000000000000007, "quality": "未知品质", "qty": 10},
          {"id": 20000000000000008, "quality": "合格品", "qty": 300},
          {"id": 20000000000000009, "quality": "次品", "qty": 10},
          {"id": 20000000000000010, "quality": "合格品", "qty": 60},
          {"id": 20000000000000011, "quality": "废品", "qty": 1}
          ]

# 作业数据(作为变化/边):一种变化可以存在多种实现方式
jobs1 = [{"id": 30000000000200001, "from": {"quality": "未知品质"}, "to": {"quality": "合格品"}, "duration": "10",
          "capacity": "10"},
         {"id": 30000000000200002, "from": {"quality": "未知品质"}, "to": {"quality": "次品"}, "duration": "10",
          "capacity": "10"},
         {"id": 30000000000200003, "from": {"quality": "良品"}, "to": {"quality": "未知品质"}, "duration": "10",
          "capacity": "10"},
         {"id": 30000000000200004, "from": {"quality": "合格品"}, "to": {"quality": "未知品质"}, "duration": "10",
          "capacity": "10"}]

jobs2 = [{"id": 30000000000200005, "from": {"quality": "合格品"}, "to": {"quality": "良品"}, "duration": "10",
          "capacity": "10"},
         {"id": 30000000000200006, "from": {"quality": "次品"}, "to": {"quality": "合格品"}, "duration": "10",
          "capacity": "10"},
         {"id": 30000000000200007, "from": {"quality": "次品"}, "to": {"quality": "废品"}, "duration": "10",
          "capacity": "10"},
         {"id": 30000000000200008, "from": {"quality": "合格品"}, "to": {"quality": "未知品质"}, "duration": "5",
          "capacity": "5"}]

# 目标数据
targets = [{"id": 40000000000000001, "from": "合格品", "to": "废品"},
           {"id": 40000000000000002, "from": "合格品", "to": "未知品质"},
           {"id": 40000000000000003, "from": "未知品质", "to": "良品"},
           {"id": 40000000000000004, "from": "未知品质", "to": "良品"},
           {"id": 40000000000000005, "from": "良品", "to": "合格品"},
           {"id": 40000000000000006, "from": "合格品", "to": "良品"},
           {"id": 40000000000000007, "from": "次品", "to": "良品"}]
