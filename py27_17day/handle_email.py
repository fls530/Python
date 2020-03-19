import os
import win32com.client as win32
import datetime
from py27_17day.handle_logg import log
import os

mail_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'New-report.html')  # 获取测试报告路径


class send_email:
    def outlook(self):
        olook = win32.Dispatch("%s.Application" % 'Outlook')
        mail = olook.CreateItem(0)
        mail.To = '530740300@qq.com'  # 收件人
        mail.CC = '18562576336@163.com'  # 抄送
        mail.Subject = str(datetime.datetime.now())[0:19] + '%s' % '接口自动化测试报告'  # 邮件主题
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        content = """
                            执行测试中……
                            测试已完成！！
                            生成报告中……
                            报告已生成……
                            报告已邮件发送！！
                            """
        mail.Body = content
        mail.Send()
        print('send email ok!!!!')
        log.info('send email ok!!!!')
