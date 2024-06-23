from collections import deque, defaultdict
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
    

if __name__ == '__main__':
    bai_3()