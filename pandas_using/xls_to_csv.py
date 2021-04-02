import pandas as pd
from pandas import Series, DataFrame

def xlsx_to_csv_pd(xlsx):
    data_xls = pd.read_excel(xlsx, index_col=0)
    data_xls.to_csv('1.csv', encoding='utf-8')


if __name__ == '__main__':
    xlsx_to_csv_pd('AI各条街的下注尺度建议.xlsx')