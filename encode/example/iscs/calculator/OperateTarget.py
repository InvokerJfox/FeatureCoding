class OperateTarget:
    pass


def merge_compress_ops(ops: list) -> list:
    """
        compress method :
            1.由于不变的特性使得各维度值正交，故压缩所有不变特征至new_ops[0];不存在则new_ops[0]=[]
            2.若仅考虑操作的原始/目标的唯一性,则该特征也是正交的,可以压缩
    :param ops:
    :return:
    """
    new_ops = [0]  # 第一个元素是代表不变的常数特征集合
    for op in ops:
        if op[0] == op[1]:
            new_ops[0] = new_ops[0] | op[0]
        else:
            compressed = False
            for new_op in new_ops[1:]:
                if op[0] & new_op[0] != 0:  # 起始态相同,对目标态增加值
                    new_op[1] = new_op[1] | op[1]
                    compressed = True
                    break
                elif op[1] & new_op[1] != 0:  # 目标态相同,对起始态增加值
                    new_op[0] = new_op[0] | op[0]
                    compressed = True
                    break

            if not compressed:  # 未压缩则新增值
                new_ops.append(op)

    return new_ops


def operate_once_target(targets: list, ops: list) -> list:
    """

    if any change in targets matched operations,return the target and the operation.
    :param targets: [['origin_state','target_state'],[next]]
    :param ops: [['origin_state','target_state'],[next]]
    :return: [target,[finish_operation]]
    """
    # 数据&格式检查
    if not (isinstance(targets, list)):
        raise ValueError("target(%s) is not a type of list" % (type(targets)))
    if not (isinstance(ops, list)):
        raise ValueError("ops(%s) is not a type of list" % (type(ops)))

    # 输入不能为空
    if not (targets or ops):
        return []

    result = []
    # 当起始目标态不变化时,则可通过满足不变化操作(ops第一项)验证,且一旦验证成功则返回
    if targets[0] & ops[0] != 0:
        result.append((targets[0], [ops[0]]))
    else:
        result.append((targets[0], []))

    # 匹配剩余操作
    for target in targets[1:]:
        valid_ops = []
        for op in ops[1:]:
            if target[0] & op[0] != 0 and target[1] & op[1] != 0:
                valid_ops.append(op)
        result.append((target, valid_ops))

    return result


def is_operated_once_target(result: list):
    """
    判断目标操作结果是否存在成功结果，'或'关系
    :param result:
    :return:
    """
    for state in result:
        if state[1] is not []:
            return True

    return False


def operated_finish_target(targets: list, ops: list, gain: list):
    """

    :param targets: 子目标需求状态操作
    :param ops: 可用状态操作
    :param gain: 状态维度间价值权重
    :return:
    """
    pass
