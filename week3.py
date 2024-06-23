from collections import defaultdict
import random

def bai_1():
    D = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    print(D)

def bai_2():
    n = int(input("Nhap vao so luong value muon nhap: "))
    dic = {}
    for i in range(n):
        dic[i] = input()
    for i in set(dic.values()):
        print(i)

def bai_3():
    n = int(input('Nhap vao so luong value muon nhap: '))
    dic = {}
    for i in range(n):
        dic[i] = int(input())
    sorted_values = sorted(dic.values(), reverse=True)
    for i in sorted_values[:3]:
        print(i)

def bai_4():
    n = input('Nhap 1 string: ')
    dic = defaultdict(int)
    for i in n:
        dic[i] += 1 
    print(dict(dic))

def bai_5():
    n, m = map(int, input('Nhap so loai cay muon luu tru gia va so luong ton tai cua chung: ').split())
    price, stock = {}, {}
    for i in range(n):
        a, b = input(), int(input())
        price[a] = b
    for i in range(m):
        a, b = input(), int(input())
        stock[a] = b
    for i in sorted(price.keys()):
        if i in stock:
            print(i, stock[i])
        else:
            print(i, 0)

def bai_6():
    dic = {}
    for i in range(1, 13):
        a = input(f'Nhap ten thang: ')
        b = 'thang ' + str(a)
        arr = []
        for j in range(20):
            arr.append(random.randint(100, 4000))
        dic[b] = arr
    print("Danh sach luong mua theo thang:")
    print(dic)

def bai_7():
    dic_a, dic_b, dic_c = {}, {}, {}

    a = int(input("Nhap so luong phan tu cua dictionary A: "))
    for _ in range(a):
        n = input("Nhap key cua A: ")
        m = int(input('Nhap value cua A: '))
        dic_a[n] = m

    b = int(input('Nhap so luong phan tu cua dictionary B: '))
    for _ in range(b):
        n = input("Nhap key cua B: ")
        m = int(input('Nhap value cua B: '))
        dic_b[n] = m

    for i in dic_a.keys():
        if i in dic_b.keys():
            max_vl = max(dic_a[i], dic_b[i])
            dic_b.pop(i)
            dic_c[i] = max_vl
        else:
            dic_c[i] = dic_a[i]

    for key, value in dic_b.items():
        dic_c[key] = value

    print("Dictionary C sau khi xu ly:", dic_c)

if __name__ == '__main__':
    n = int(input('Nhap 1, 2, 3 ... tuong ung voi cac bai 1, 2, 3..: '))
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
    else:
        print('khong chinh xac nhap lai')
