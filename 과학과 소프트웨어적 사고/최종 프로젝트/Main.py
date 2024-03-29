import json
from Phonebook import Phonebook
from Message import *


if __name__ == '__main__':
    try:
        json_file = open('./info.json', encoding='utf-8')
        json_data = json.load(json_file)
        json_file.close()
    except FileNotFoundError:
        json_file = open('./info.json', 'w', encoding='utf-8')
        json.dump([], json_file, indent="\t")
        json_file.close()
        json_file = open('./info.json', encoding='utf-8')
        json_data = json.load(json_file)
        json_file.close()

    except IOError:
        print_file_error_message()
        exit()

    phonebook = Phonebook(json_data)
    select_menu = 0
    print_information()

    while(True):
        print_main_menu()
        select_menu = input(" - 선택하려는 메뉴 번호를 입력해주세요: ")

        try:
            page_num = int(select_menu)
            if page_num == 1:
                while True:
                    if phonebook.add_information():
                        break

            elif page_num == 2:
                phonebook.modify_information()

            elif page_num == 3:
                phonebook.delete_information()

            elif page_num == 4:
                init_flag = False
                while(True):
                    print_init_message()
                    init_input = input()
                    print("")

                    if init_input == "예":
                        init_flag = True
                        break
                    elif init_input == "아니오":
                        init_flag = False
                        break
                    else:
                        print_tof_error_message()
                        continue
                if init_flag:
                    phonebook.delete_all_information()

            elif page_num == 5:
                phonebook.search_information()

            elif page_num == 6:
                phonebook.search_all_information()

            elif page_num == 7:
                exit_flag = False

                while(True):
                    print_before_exit_message()
                    exit_input = input()
                    print("")

                    if exit_input == "예":
                        exit_flag = True
                        break
                    elif exit_input == "아니오":
                        exit_flag = False
                        break
                    else:
                        exit_flag = False
                        print_tof_error_message()
                        continue

                if exit_flag:
                    print(" ----- 프로그램을 종료합니다. -----".center(100))
                    print("")
                    break

            else:
                print_invalid_input_error(scope=7)
        except ValueError:
            print_invalid_input_error(scope=7)
