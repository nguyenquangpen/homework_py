from collections import deque, defaultdict
import os

def bai_1():
    try:
        a, b = map(int, input('nhap 2 so nguyen: ').split())
        print(f'Kết quả của {a} / {b} là: {a / b}')

    except ValueError:
        print('nhap lai 2 so nguyen: ')

    except ZeroDivisionError as ex:
        print('loi', ex)

def bai_2():
    try:
        a, b, c = map(int, input('nhap do dai 2 canh tam giac: ').split())
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('do dai cac canh phai lon hon 0')
        if a+b <= c or a+c <= b or b+c <= a:
            raise ValueError('do dai phai la 3 canh cua tam giac')
    except ValueError as ve:
        print(f'Lỗi: {ve}')
    except Exception as e:
        print(f'Lỗi không xác định: {e}')

def bai_3():
    dic, count = defaultdict(int), 0
    try:
        while True:
            n = input('nhap so nguyen or end de ket thuc: ')
            if n == 'end':
                break
            try:
                n = int(n)
                if n < 0:
                    raise ValueError('loi so am !!!')
            except ValueError as ex:
                print('loi nhap so')
                continue
            dic[n] += 1
            if dic[n] == 4:
                raise ValueError('loi nhap lap')

            if n % 2 == 0:
               count += 1

            if count == 5:
                raise ValueError('loi nhap chan')

    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print('Lỗi không xác định:', ex)

def bai_4():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\file_bt.txt', 'r', encoding= 'utf-8') as f:
        for _ in range(5):
            line = f.readline()
            if not line:
                break
            print(line)

def bai_5():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\file_bt.txt', 'r', encoding= 'utf-8') as f:
        lines = f.readlines()
        count = len(lines)
        if count <= 5:
            for line in lines:
                print(line)
        else:
            for line in lines[-5:]:
                print(line)
def bai_6():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\file_bt.txt', 'r', encoding= 'utf-8') as f:
        lines = f.readlines()
        max_vl = float('-inf')
        for i in range(len(lines)):
            if max_vl < len(lines[i]):
                max_vl = len(lines[i])
                tmp = i
        print(lines[tmp])
def bai_7():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\file_bt.txt', 'r', encoding= 'utf-8') as f:
        lines = f.read().split()
        print(max([len(i) for i in lines]))
def bai_8():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\file_bt.txt', 'r', encoding= 'utf-8') as f:
        dic = defaultdict(int)
        lines = f.read()
        for i in lines:
            if i not in (' ', '\n', '.', ','):
                dic[i] += 1 
        for char, count in dic.items():
            print(f"{char} : {count}")
def bai_9():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\file_bt.txt', 'r', encoding= 'utf-8') as f:
        dic = defaultdict(int)
        lines = f.read()
        for i in sorted(lines):
            if i not in (' ', '\n', '.', ','):
                dic[i] += 1 
        for char, count in dic.items():
            print(f"{char} : {count}")
def bai_10():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\abc.txt', 'r', encoding= 'utf-8') as f:
        lines = f.read()
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\xyz.txt', 'w', encoding= 'utf-8') as f:
        f.write(lines.upper)
def bai_11():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\abc.txt', 'r', encoding= 'utf-8') as f:
        lines = f.read()
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\number.txt', 'a', encoding= 'utf-8') as f:
        f.write(lines)
def bai_12():
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\abc.txt', 'r', encoding= 'utf-8') as f:
        lines_abc = f.read()
    with open(r'C:\school_phenikaa\year_1\kỳ 3\python\xyz.txt', 'w', encoding= 'utf-8') as f:
        line_xyz = f.read()
    if line_xyz == lines_abc:
        print('2 tep tin same nhau')
    else:
        print('khac nhau')
def bai_13():
    url = os.getcwd()
    dic, count = {}, 1
    files = [f for f in os.listdir(url) if os.path.isfile(os.path.join(url, f))]
    for file in files:
        file_path = os.path.join(url, file)
        with open(file_path, 'r', encoding = 'utf-8') as f:
            cmd = f.read()
        found = False
        for key, value in dic.items():
            if cmd in value:
                dic[key].append(file)
                found = True
                break
        if not found:
            dic[count] = [file]
            count += 1
    for key, value in dic.items():
        if len(value) > 1:
            print(f"Nhóm {key}: {', '.join(value)}")


if __name__ == '__main__':
    n = int(input('nhap so 1, 2, 3, 4... tuong ung voi so bai: '))
    if n == 1:
        bai_1()
    elif n == 2:
        bai_2()
    elif n == 3:
        bai_3()
    elif n == 4:
        bai_4()
    elif n == 5:
        bai_5()
    elif n == 6:
        bai_6()
    elif n == 7:
        bai_7()
    elif n == 8:
        bai_8()
    elif n == 9:
        bai_9()
    elif n == 10:
        bai_10()
    elif n == 11:
        bai_11()
    elif n == 12:
        bai_12()
    elif n == 13:
        bai_13()
    else:
        print("khong say ra")