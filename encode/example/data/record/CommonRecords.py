# 业务单位定义
define_business_unit = [{"id": 10000000000001001, "dimension": "business_unit", "defined": '仓储方'},
                        {"id": 10000000000002001, "dimension": "business_unit", "defined": '张三'},
                        {"id": 10000000000002002, "dimension": "business_unit", "defined": '李四'},
                        {"id": 10000000000002003, "dimension": "business_unit", "defined": '王五'},
                        {"id": 10000000000003001, "dimension": "business_unit", "defined": '顺丰'},
                        {"id": 10000000000020004, "dimension": "business_unit", "defined": '小一'},
                        {"id": 10000000000020005, "dimension": "business_unit", "defined": '小q'},
                        {"id": 10000000000020006, "dimension": "business_unit", "defined": '小w'},
                        {"id": 10000000000020007, "dimension": "business_unit", "defined": '小e'},
                        {"id": 10000000000020008, "dimension": "business_unit", "defined": '小r'},
                        {"id": 10000000000020009, "dimension": "business_unit", "defined": '小t'},
                        {"id": 10000000000020010, "dimension": "business_unit", "defined": '小y'},
                        {"id": 10000000000020011, "dimension": "business_unit", "defined": '小u'},
                        {"id": 10000000000020012, "dimension": "business_unit", "defined": '小i'},
                        {"id": 10000000000020013, "dimension": "business_unit", "defined": '小o'},
                        {"id": 10000000000020014, "dimension": "business_unit", "defined": '小a'},
                        {"id": 10000000000020015, "dimension": "business_unit", "defined": '小s'}]

# 品质定义
define_quality = [{"id": 10000000001500001, "dimension": "quality", "defined": "未知品质"},
                  {"id": 10000000001500001, "dimension": "quality", "defined": "良品"},
                  {"id": 10000000001500001, "dimension": "quality", "defined": "合格品"},
                  {"id": 10000000001500001, "dimension": "quality", "defined": "次品"},
                  {"id": 10000000001500001, "dimension": "quality", "defined": "废品"}]

# 操作定义
define_operations = [
    {"id": 10000030000000001, "dimension": "operation", "type": "quality", "from": "未知品质", "to": "合格品"},
    {"id": 10000030000000002, "dimension": "operation", "type": "quality", "from": "未知品质", "to": "次品"},
    {"id": 10000030000000003, "dimension": "operation", "type": "quality", "from": "良品", "to": "未知品质"},
    {"id": 10000030000000004, "dimension": "operation", "type": "quality", "from": "合格品", "to": "未知品质"},
    {"id": 10000030000000005, "dimension": "operation", "type": "quality", "from": "合格品", "to": "良品"},
    {"id": 10000030000000006, "dimension": "operation", "type": "quality", "from": "次品", "to": "合格品"},
    {"id": 10000030000000007, "dimension": "operation", "type": "quality", "from": "次品", "to": "废品"}]

# 消费物数据
goods = [{"id": 20000000000000001, "quality": "未知品质"},
         {"id": 20000000000000002, "quality": "未知品质"},
         {"id": 20000000000000003, "quality": "良品"},
         {"id": 20000000000000004, "quality": "未知品质"},
         {"id": 20000000000000005, "quality": "次品"},
         {"id": 20000000000000006, "quality": "良品"},
         {"id": 20000000000000007, "quality": "未知品质"},
         {"id": 20000000000000008, "quality": "合格品"},
         {"id": 20000000000000009, "quality": "次品"},
         {"id": 20000000000000010, "quality": "合格品"},
         {"id": 20000000000000011, "quality": "废品"}
         ]

# 作业数据(每个作业"仅一种明确"的作业方式)
jobs = [{"id": 30000000000200001, "from": "未知品质", "to": "合格品"},
        {"id": 30000000000200002, "from": "未知品质", "to": "次品"},
        {"id": 30000000000200003, "from": "良品", "to": "未知品质"},
        {"id": 30000000000200004, "from": "合格品", "to": "未知品质"},
        {"id": 30000000000200005, "from": "合格品", "to": "良品"},
        {"id": 30000000000200006, "from": "次品", "to": "合格品"},
        {"id": 30000000000200007, "from": "次品", "to": "废品"}]
