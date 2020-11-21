import sys
import openpyxl
from pathlib import Path

source_list = []


def main():
    path = get_source_link()
    print(show_source_to_user(path))


def get_source_link():
    #path = input("Insert path to source: ")
    path = "/home/jkafka/qa_finder_files/source.xlsx"
    return path


def source_max_row_get(path):
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_row = sheet_obj.max_row
    return max_row, sheet_obj


def source_list_data_get(path):
    max_row, sheet_obj = source_max_row_get(path)
    for i in range(1, max_row + 1):
        cell_obj = sheet_obj.cell(row=i, column=2)
        source_list.append(cell_obj.value)
    return source_list


def show_source_to_user(path):
    source_data = source_list_data_get(path)
    return source_data


def approve_source():
    pass


def get_target_from_pdf():
    pass


def get_pdf_name():
    pass


def make_clean_text():
    pass


def source_and_target_compare():
    pass


def compare_result():
    pass


if __name__ == '__main__':
    main()
