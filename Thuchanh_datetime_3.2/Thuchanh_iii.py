from datetime import datetime
s=input(print('Nhap vao chuoi ngay(ep 18 2019 2:43PM): '))
#s = 'Sep 18 2019 2:43PM'
date_change=datetime.strptime(s, '%b %d %Y %I:%M%p')

print('Chuỗi sau khi chuyển sang kiểu datetime: ',date_change)
print('Kiểu dữ liệu: ',type(date_change))