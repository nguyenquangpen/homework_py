# from curses.ascii import isdigit
import random
import math

def in_ptu():
    for i in range(1, 99):
        print(i)

def bai2():
    for i in range(1, 199):
        if i % 2 != 0:
            print(i)

def bai_3(tmp):
    print("Max:", max(tmp))
    print("Min:", min(tmp))
    print("Total elements:", len(tmp))

def bai4():
    danh_sach_hoc_sinh = []
    while True:
        ten = input("Nhap ten hoc sinh (enter de ket thuc): ").split(' ')
        if ten == ['']:
            break
        danh_sach_hoc_sinh.append(ten)
    for num in danh_sach_hoc_sinh:
        print('ho: ', num[0])
        print('ten: ', num[2])

def bai_5():
    N = int(input("Nhap so N: "))
    tmp = [i for i in range(1, N) if N % i == 0]
    for i in tmp:
        print(i)

def uoc_cua_so(n):
    uoc = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            uoc.add(i)
            uoc.add(n // i)
    return uoc

def bai_6(a, b):
    if a <= 0 or b <= 0:
        return "Both numbers must be positive integers."
    uoc_a = uoc_cua_so(a)
    uoc_b = uoc_cua_so(b)
    return uoc_a & uoc_b

def bai_7():
    chuoi = input("Nhap cac so cach nhau boi ';': ")
    result = set(chuoi.split(";"))
    return len(result)

def bai_8():
    nguoi_dung = list(map(int, input("Chon 6 so cach nhau boi khoang trang: ").split()))
    giai = random.sample(range(1, 46), 6)  
    tmp = len(set(nguoi_dung) & set(giai))
    print("Winning numbers:", giai)
    return "Win" if tmp >= 5 else "False"

def is_prime(n): 
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def bai_10():
    a, b = map(int, input("Enter range (a b): ").split())
    for num in range(a, b + 1):
        if is_prime(num):
            print(num)

def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

def bai_11():
    a, b = map(int, input().split())
    print(f'ucln: {ucln(a, b)}, bcnn: {bcnn(a, b)}')

def bai_12():
    tmp = []
    while True:
        x = int(input())
        if x <= 0:
            break
        tmp.append(x)
    gcd, bc = tmp[0], tmp[0]
    for i in range(1, len(tmp)):
        gcd = ucln(gcd, tmp[i])
        bc = bcnn(bc, tmp[i])
    print(f'ucln: {gcd}, bcnn: {bc}')

def bai_13():
    tmp = []
    while True:
        x = int(input())
        if x <= 0:
            break
        tmp.append(x)
    print(f'so luong {len(tmp)} min: {min(tmp)} max: {max(tmp)}')

def bai_14():
    txt = input()
    while len(txt) < 3 or txt[-3:] != '!!!':
        txt += '!'
    print(txt)

def bai_15():
    tmp = input().split(' ')
    for i in tmp:
        print(i)

def bai_16():
    tmp = input().split(' ')
    print(f'ho: {tmp[0]}, ten: {tmp[-1]}')

def bai_17():
    tmp = input()
    temp = ""
    for i in tmp:
        if not i.isdigit():
            temp += i
    print(temp)

def bai_18():
    tmp = [input() for _ in range(9)]
    max_vl = max(len(x) for x in tmp)
    for i in tmp:
        if len(i) == max_vl:
            print(i)

def bai_19():
    txt = {}
    tmp = list(map(str, input('nhap cac tu co dau cach: ').split()))
    for word in tmp:
        if word in txt:
            txt[word] += 1
        else:
            txt[word] = 1

def bai_21():
    txt = ''
    n = input("nhap chuoi s: ")
    for i in range(len(n)):
        txt += '?'
    print(txt)

def bai_22():
    n = input()
    a, b = 0, len(n) - 1
    while a < b:
        if n[a] != n[b]:
            return False
        a += 1
        b -= 1
    return True

def bai_23():
    tmp = list(map(str, input('nhap cac tu co dau cach: ').split()))
    tmp.sort()
    for i in tmp:
        print(i)

def bai_24():
    tmp = input('nhap cac so nhi phan cach nhau boi dau phay:').split(',')
    for i in tmp:
        print(i)

def bai_25():
    n = input('nhap dia chi email: ')
    if '@gmail.com' in n:
        print('hop le')
    else:
        print('no')

def fib(n):
    a, b = 0, 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def bai_26():
    n = int(input('nhap so nguyen N: '))
    for num in range(n):
        if fib(num):
            print(num)

if __name__ == "__main__":
    k = int(input("Nhap 1, 2, 3, 4, 5... de chay cac bai tuong ung: "))
    if k == 1:
        in_ptu()
    elif k == 2:
        bai2()
    elif k == 3:
        tmp = list(map(int, input("Nhap cac so cach nhau boi khoang trang: ").split()))
        bai_3(tmp)
    elif k == 4:
        bai4()
    elif k == 5:
        bai_5()
    elif k == 6:
        a = int(input("Nhap so a: "))
        b = int(input("Nhap so b: "))
        print(bai_6(a, b))
    elif k == 7:
        print(bai_7())
    elif k == 8:
        print(bai_8())
    elif k == 9:
        print(is_prime(int(input("Nhap so N: "))))
    elif k == 10:
        bai_10()
    elif k == 11:
        bai_11()
    elif k == 12:
        bai_12()
    elif k == 13:
        bai_13()
    elif k == 14:
        bai_14()
    elif k == 15:
        bai_15()
    elif k == 16:
        bai_16()
    elif k == 17:
        bai_17()
    elif k == 18:
        bai_18()
    elif k == 19:
        bai_19()
    elif k == 21:
        bai_21()
    elif k == 22:
        print(bai_22())
    elif k == 23:
        bai_23()
    elif k == 24:
        bai_24()
    elif k == 25:
        bai_25()
    elif k == 26:
        bai_26()
    else:
        print("Lua chon khong hop le!")
