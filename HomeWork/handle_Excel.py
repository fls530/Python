import openpyxl


class HandleExcel:
    """ 用来操作Excel的类"""

    def __init__(self, filename, sheetname):
        """
        初始化
        :param filename: 文件名
        :param sheetname: 表单名
        将加载excel工作簿对象和获取表单写在构造函数里
        """
        self.filename = filename
        self.sheetname = sheetname
        self.wb = openpyxl.load_workbook(self.filename)
        self.sh = self.wb[self.sheetname]

    def read_data(self):
        """读取excel中的数据"""

        row_data = list(self.sh.rows)  # 按行获取所有的数据,转换为列表
        # 创建一个列表,保存所有的用例数据  数据
        cases_data = []
        # 获取表单中的表头,放入title列表
        title = []
        for i in row_data[0]:
            title.append(i.value)
        # 获取除表头之外的所有数据
        for item in row_data[1:]:
            values = []
            for j in item:
                values.append(j.value)
            # 将该行的数据和title打包成字典,并且将字典添加到cases_data
            cases_data.append(dict(zip(title, values)))
        # 返回读取的所有数据
        return cases_data

    def write_data(self, row, col, value):
        """
        将测试结果写入excel
        :param row:
        :param col:
        :param value:
        :return:
        """
        # 根据行列写入内容
        self.sh.cell(row=row, column=col, value=value)
        # 把工作簿保存为文件
        self.wb.save(self.filename)


if __name__ == '__main__':
    excel = HandleExcel('Cases.xlsx', 'login')
    res = excel.read_data()
    print(res)
    # excel.write_data(row=6, col=6, value="python")
