import os

import xlrd

from mysite.mysite import settings


def data_from_xlsx(path):
    vac_name = "web-разработчик"
    path = os.path.join(settings.MEDIA_ROOT, str().replace('/', '\\'))
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_index(0)
    print(ws)
    excel_data = list()
    for row in range(ws.nrows):
        row_data = list()
        for col in range(ws.ncols):
            row_data.append(ws.cell(row, col).value)
        excel_data.append(row_data)
    return excel_data, vac_name