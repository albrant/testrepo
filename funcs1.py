import csv

res = []


def read_csv_file() -> dict:
    with open('data.csv', encoding='utf-8') as f:
        data = []
        st = f.readlines()
        for i in st:
            st_in = i.split(';')
            tpl = tuple(j.strip() for j in st_in)
            data.append(tpl)

    return data


def write_csv_file(data: list):
    st = ''
    for el in data:
        for j in el:
            st += j + ';'
        st = st[:-1] + '\n'

    with open('data_final.csv', 'w', encoding='utf-8') as f:
        f.write(st)
