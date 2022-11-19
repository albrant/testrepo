
def read_txt_file():
    file_name = "data.txt"
    data = list()
    with open(file_name, encoding='utf-8') as file:

        current = file.readline()
        while len(current) > 0:
            current_lst = []
            while current != "\n" and len(current) > 0:
                current = current.replace("\n", "")
                current_lst.append(current)
                current = file.readline()
            data.append(tuple(current_lst))
            current = file.readline()

    return data

def write_txt_file(data: list):
    file_name = "data.txt"
    with open(file_name, "a", encoding="utf-8") as file:
        file.writelines("\n")
        file.writelines("\n")
        for record in data:
            for string in record:
                file.writelines(string + "\n")
            file.writelines("\n")
