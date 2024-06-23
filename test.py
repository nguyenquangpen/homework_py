import math

def average(a1, a2, a3, a4, a5):  # bài 1
    return (a1 + a2 + a3 + a4 + a5) / 5

def area(a1, a2, a3):  # bài 2
    p = (a1 + a2 + a3) / 2
    S_tg = math.sqrt(p * (p - a1) * (p - a2) * (p - a3))
    return S_tg

def area2(x1, y1, x2, y2, x3, y3):  # bài 3
    dien_tich = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
    return dien_tich

def total(N):  # bài 4
    return sum(map(int, str(N)))

def fib(N):  # bài 5
    a, b = 0, 1
    while a < N:
        a, b = b, a + b
        if a == N:
            return True
    return False

def giaithua(N):  # bài 6
    return math.factorial(N)

def diem_tb(toan, ly, hoa):  # bài 7
    tb = (toan + ly + hoa) / 3
    if tb < 3.5:
        return "Yếu"
    elif 3.5 <= tb < 5:
        return "Kém"
    elif 5 <= tb < 6.5:
        return "Trung bình"
    elif 6.5 <= tb < 8:
        return "Khá"
    elif 8 <= tb < 9:
        return "Giỏi"
    else:
        return "Xuất sắc"

def bai_8(a1, a2, a3):  # bài 8
    max_vl = max(a1, a2, a3)
    if a1 == max_vl:
        print(a1)
    elif a2 == max_vl:
        print(a2)
    elif a3 == max_vl:
        print(a3)
    print(max_vl)

def tinh_so_ngay_thang(m, y):
    so_ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
        return 29  
    return so_ngay[m - 1]

def tinh_ngay_tiep_theo(d, m, y):  # bài 9
    so_ngay_thang = tinh_so_ngay_thang(m, y)
    if d < so_ngay_thang:
        d += 1
    else:
        d = 1
        if m == 12:
            m = 1
            y += 1
        else:
            m += 1
    return d, m, y


if __name__ == "__main__":
    print("Nhập 1, 2, 3, 4, 5, 6, 7, 8, 9 tương ứng với các bài 1, 2, 3, ...:")
    num = int(input())
    if num == 1:
        print("Nhập 5 số: ")
        a1, a2, a3, a4, a5 = map(int, input().split())
        print(average(a1, a2, a3, a4, a5))
    elif num == 2:
        print("Nhập các cạnh: ")
        a1, a2, a3 = map(int, input().split())
        print(area(a1, a2, a3))
    elif num == 3:
        print("Nhập tọa độ 3 điểm: ")
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        print(area2(x1, y1, x2, y2, x3, y3))
    elif num == 4:
        print("Nhập N: ")
        N = int(input())
        print(total(N))
    elif num == 5:
        print("Nhập N: ")
        N = int(input())
        print(fib(N))
    elif num == 6:
        print("Nhập N: ")
        N = int(input())
        print(giaithua(N))
    elif num == 7:
        print("Nhập điểm 3 môn: ")
        toan, ly, hoa = map(int, input().split())
        print(diem_tb(toan, ly, hoa))
    elif num == 8:
        print("Nhập 3 số: ")
        a1, a2, a3 = map(int, input().split())
        bai_8(a1, a2, a3)
    elif num == 9:
        print("Nhập ngày, tháng, năm: ")
        d, m, y = map(int, input().split())
        d, m, y = tinh_ngay_tiep_theo(d, m, y)
        print(f"Ngày tiếp theo là: {d}/{m}/{y}")
    else:
<<<<<<< HEAD
        print("khong thoa mãn.")
=======
        print("không có gtri thoa man")
>>>>>>> 5cc479cd381c2cbeee44fb6eb822d1caa00ae3e2
