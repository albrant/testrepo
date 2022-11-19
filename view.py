from funcs1 import read_csv_file, write_csv_file
from funcs2 import read_txt_file, write_txt_file

data = [('Иванов', 'Иван', 'Васильевич', 'слесарь', 'слесарный отдел', 'Рога и копыта'), (), (), ()]


def read_data():
    data = read_csv_file()
    return data

def print_data():
    pass

def run():
    data = read_data(type='csv')
    data.sort()
    print_data(data)
    write_data(data)

