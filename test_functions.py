from dateutil.parser import parse
from tempfile import TemporaryFile
import xlwt


# functions
def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False


# create xls
def xls_output(filename, sheetname, data_dict):
    book = xlwt.Workbook()
    sh = book.add_sheet(sheetname)

    row_number = 0
    for data in data_dict:
        try:
            dated_data = [data] + data_dict[data]
            for column_number in range(0, len(dated_data) - 1):
                sh.write(row_number, column_number, dated_data[column_number])
                # print('saving:', dated_data[column_number])
        except IndexError:
            pass
        row_number += 1

    book.save(filename)
    book.save(TemporaryFile())
