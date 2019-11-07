import os

def clear():
    # os.system('cls' if os.name == 'nt' else 'clear')  밑에 If문(4줄)을 한줄로 하면^^

    if os.name == 'nt':  # windows 기반
        os.system('cls')
    else:  # posix : 리눅스 기반
        os.system('clear')