so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
a = so1
b = so2
while b != 0:
    r = a % b
    a = b
    b = r
ucln = a
bcnn = (so1 * so2) // ucln
print("Bội chung nhỏ nhất của là:", bcnn)
