# code=utf-8
from datetime import date
import xlrd
from xlutils.copy import copy

class ExcelUtil(object):
    def __init__(self, excel_path=None, index=None) -> None:
        if excel_path is None:
            self.excel_path = "F:\\projects\\selenium\\config\\testData.xlsx"
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    # 获取excel数据
    def get_data(self):
        results = []
        rows = self.get_lines()
        if rows:
            for i in range(self.get_lines()):
                col = self.table.row_values(i)
                results.append(col)
                print(col)
        return results

    def read_excel(self):
        pass

    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    def get_cols_value(self, row, cell):
        if self.get_lines() > row:
            date = self.table.cell(row, cell).value
            return date
        return None

    def has_next(self):
        pass

    def write_data(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data  = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    el = ExcelUtil("F:\\projects\\selenium\\config\\keyword.xls")
    print(el.get_cols_value(8, 9))
    