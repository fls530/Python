import unittest
import os
from BeautifulReport import BeautifulReport


suite = unittest.defaultTestLoader.discover(os.path.dirname(os.path.abspath(__file__)))
br = BeautifulReport(suite)
br.report("刘宝龙接口--测试报告", 'New-report.html')
