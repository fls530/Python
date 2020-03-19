import unittest
import os
from BeautifulReport import BeautifulReport
from py27_17day.handle_email import send_email

send_email = send_email()
suite = unittest.defaultTestLoader.discover(os.path.dirname(os.path.abspath(__file__)))
br = BeautifulReport(suite)
br.report("日志--测试报告", 'New-report.html')
send_email.outlook()