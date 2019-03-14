# file : main.py

from menu import show_menu
from student_info import *

def main():
    infos = []  # 此列表用于保存学生数据
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            output_student(infos)
        elif s == '3':
            delete_student(infos)
        elif s == '4':
            modify_student_score(infos)
        elif s == '5':
            output_by_score_desc(infos)
        elif s == '6':
            output_by_score_asc(infos)
        elif s == '7':
            output_by_age_desc(infos)
        elif s == '8':
            output_by_age_asc(infos)
        elif s == '9':
            infos = read_from_file()
        elif s == '10':
            save_to_file(infos)  # 保存
        elif s == 'q':
            break

main()
   