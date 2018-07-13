import time
import unittest

from cn.ivker.encode.tester import CaseTester

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [CaseTester("ttt_ddd")]
    suite.addTests(tests)

    # 保存测试报告
    timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    with open('TextReport' + timestamp + '.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
