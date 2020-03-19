import unittest
from HomeWork.Myddt import ddt, data
from HomeWork.handle_Excel import HandleExcel
from HomeWork.login import login_check


@ddt
class LoginCheckTestCase(unittest.TestCase):
    excel = HandleExcel('Cases.xlsx', 'login')
    cases = excel.read_data()

    @data(*cases)
    def test_login_check(self, case):
        # 准备用例数据
        expected = eval(case['expected'])
        case_data = eval(case['data'])
        # 代用功能函数
        res = login_check(*case_data)
        # 断言
        try:
            self.assertEqual(expected, res)
            Result = 'Pass'
        except AssertionError as e:
            Result = 'Fail'
            raise e
        finally:
            self.excel.write_data(case['case_id'] + 1, 5, str(res))
            self.excel.write_data(case['case_id'] + 1, 5, Result)
