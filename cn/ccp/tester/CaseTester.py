import unittest


class CaseTester(unittest.TestCase):
    def tearDown(self):
        pass  # 每个测试用例执行之后做操作

    def setUp(self):
        pass  # 每个测试用例执行之前做操作

    @classmethod
    def tearDownClass(cls):
        pass  # 所有test运行完后运行一次

    @classmethod
    def setUpClass(cls):
        pass  # 所有test运行前运行一次

    def ttt_ddd(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
