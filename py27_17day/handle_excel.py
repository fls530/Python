import openpyxl


class HandleExcel:
    def __init__(self, filename, sheetname):
        """
        初始化
        :param filename:  文件名
        :param sheetname: sheet页
        """
        self.filename = filename
        self.sheetname = sheetname
        self.wb = openpyxl.load_workbook('cases.xlsx')
        self.sh = self.wb[self.sheetname]

    def read_excel(self):
        """ 读取excel"""
        # 选择表单
        dataexcel = []
        title = []
        # 获取sheet页第一行作为title
        data = list(self.sh.rows)
        for item in data[0]:
            title.append(item.value)

        # 获取除第一行以外的用例数据
        for i in data[1:]:
            casedata = []
            for v in i:
                casedata.append(v.value)
            dataexcel.append(dict(zip(title, casedata)))
        return dataexcel

    def write_excel(self, row, col, value):
        """
            写入excel
        :param row: 传入的行
        :param col: 传入的列
        :param value: 传入的值
        :return:
        """

        self.sh.cell(row=row, col=col, value=value)
        self.wb.save(self.filename)


if __name__ == '__main__':
    excel = HandleExcel("cases.xlsx", 'register')
    res = excel.read_excel()
    print(res)
