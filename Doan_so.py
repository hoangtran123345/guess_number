import random

def doan_so(x):
    print("Chuong trinh doan so tu 1 den {}".format(x))
    random_number = random.randint(1, x)
    kq = False
    so_lan_doan = 0
    while not kq:
        doan = int(input("Hay nhap so can doan : "))
        if doan > x or doan < 1: 
            print("Ban phai nhap so trong trong khoang da cho, hay nhap lai : ")
            continue
    
        so_lan_doan += 1

        if doan > random_number:
            print("So nay lon hon so can doan, hay nhap lai : ")
        elif doan < random_number:
            print("So nay nho hon so hon so can doan, hay nhap lai : ")
        else:
            print("Ban da doan dung, ket qua la {}".format(doan))
            kq = True
    return so_lan_doan

so_lan_doan = doan_so(20)
print("So lan doan la : {}".format(so_lan_doan))


