import unittest
from py27_17day.Myddt import ddt, data
from py27_17day.handle_excel import HandleExcel
from py27_17day.register import register
from py27_17day.handle_logg import log

@ddt
class LoginCheckTestCase(unittest.TestCase):
    excel = HandleExcel('cases.xlsx', 'register')
    cases = excel.read_excel()

    @data(*cases)
    def test_login_check(self, case):
        # 准备用例数据
        expected = eval(case['expected'])
        case_data = eval(case['data'])
        # 代用功能函数
        res = register(*case_data)
        Result = 'Fail'
        # 断言
        try:
            self.assertEqual(expected, res)
            Result = 'Pass'
            log.debug("用例通过")
        except AssertionError as e:
            log.error(e)
            raise e
        finally:
            self.excel.write_excel(case['case_id'] + 1, 5, str(res))
            self.excel.write_excel(case['case_id'] + 1, 5, Result)
