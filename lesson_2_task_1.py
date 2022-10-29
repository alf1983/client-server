import csv
import re

from chardet import detect

INFO_FILES = ['info_1', 'info_2', 'info_3', ]
REG_SYS_PROD = r"(?:Изготовитель\sсистемы\:\s+)(.+)"
REG_OS = r"(?:Название\sОС\:\s+)(.+)"
REG_PROD_CODE = r"(?:Код\sпродукта\:\s+)(.+)"
REG_SYS_TYPE = r"(?:Тип\sсистемы\:\s+)(.+)"
MAIN_DATA_HEADER = ["Изготовитель системы", 'Название ОС', 'Код продукта', 'Тип системы']


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [MAIN_DATA_HEADER, ]
    file_names_list = []
    for info_file in INFO_FILES:
        with open(info_file + '.txt', 'rb') as file_bytes:
            content = file_bytes.read()
        encoding = detect(content)['encoding']
        with open(info_file + '.txt', 'r', encoding=encoding) as file:
            content = file.read()
            info_line = re.search(REG_SYS_PROD, content)
            os_prod_list.append(info_line.group(1))
            info_line = re.search(REG_OS, content)
            os_name_list.append(info_line.group(1))
            info_line = re.search(REG_PROD_CODE, content)
            os_code_list.append(info_line.group(1))
            info_line = re.search(REG_SYS_TYPE, content)
            os_type_list.append(info_line.group(1))
    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
        current_f_n = 'main_data_' + str(i + 1) + '.csv'
        with open(current_f_n, 'w', encoding='utf-8') as main_data_file:
            main_data_writer = csv.writer(main_data_file)
            main_data_writer.writerows(main_data)
        main_data = [MAIN_DATA_HEADER, ]
        file_names_list.append(current_f_n)
    return file_names_list
    #         print("=" * 10)
    # print(os_prod_list)
    # print(os_name_list)
    # print(os_code_list)
    # print(os_type_list)


def write_to_csv(file):
    info_files_list = get_data()
    result = [MAIN_DATA_HEADER, ]
    for file_name in info_files_list:
        with open(file_name, 'r', encoding='utf-8') as f_n:
            f_n_reader = csv.reader(f_n)
            next(f_n_reader)
            for row in f_n_reader:
                result.append(row)
    f_n_writer = csv.writer(file)
    f_n_writer.writerows(result)


with open('result_info.csv', 'w', encoding='utf-8') as f_r_n:
    write_to_csv(f_r_n)
