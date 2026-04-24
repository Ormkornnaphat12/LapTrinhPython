print('--- Viet ham nhan tham so 1 so nguyen duong n. tinh hang thu n cua chuoi Fibonaci ---')
def Fibonaci(n):
    if n==0 :
        return 0
    if n==1:
        return 1
    return Fibonaci(n-1) + Fibonaci(n-2)
nhap_n = input('Nhap vao so nguyen duong n: ')
n = int(nhap_n)
print(f"So Fibonaci thu {n} = ", Fibonaci(n))