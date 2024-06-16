def in_ptu():
    for i in range(1, 99):
        print(i)
def bai2():
    for i in range(1, 199):
        if (i % 2 != 0):
            print(i)

def bai_3(tmp):
    print(max(tmp))
    print(min(tmp))
    total = 0
    for i in tmp:
        total += 1
    print(total)

def bai4():
    danh_sach_hoc_sinh = []
    while True:
        ten = input("nhap ten hs: ")
        if ten == "":
            break 
        danh_sach_hoc_sinh.append(ten)
    for i in danh_sach_hoc_sinh:
        print(i)

def bai_5():
    N = int(input())
    tmp = [i for i in range(1, N) if N % i == 0]
    for i in tmp:
        print(i)

def bai_6():
    a, b = map(int, input("nhap 2 so a, b: ").split())
    max_vl = max(a, b)
    for 

