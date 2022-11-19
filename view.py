from funcs1 import read_csv_file, write_csv_file
from funcs2 import read_txt_file, write_txt_file


def read_data(type):
    if type == 'csv':
        data = read_csv_file()
    elif type == 'txt':
        data = read_txt_file()
    return data


def print_data(data):
    for i in range(len(data)):
        print(
            f'\nФамилия: {data[i][0]}, Имя: {data[i][1]}, Отчество: {data[i][2]}, Должность: {data[i][3]}, Отдел: {data[i][4]}, Фирма: "{data[i][5]}"\n')


def write_data():
    pass


def run():
    data = read_data(type='csv')
    data.sort()
    print_data(data)
    write_data(data)
