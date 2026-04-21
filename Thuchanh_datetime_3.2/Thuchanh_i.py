from datetime import*
now=datetime.now()
week_of_month = (now.day - 1) // 7 + 1
print('Năm hiện tại: ', datetime.now().strftime("%Y"))
print('Tháng hiện tai: ',datetime.today().month)
print('Tuần hiện tại là tuần thứ mấy trong năm: ',datetime.now().strftime("%U"))
print('Tuần hiện tại là tuần thứ mấy trong tháng: ',week_of_month)
t2= date(year=2026, month=1, day=1)
t1=date(year=2026, month=4, day=21)
t3=abs(t1-t2)
print('Ngày hiện tại là ngày thứ mấy trong năm:',t3)
print('Ngày dương lịch hiện tại là ngày: ',datetime.today().day)
print('Thứ của ngày hiện tại: ',datetime.now().strftime("%A"))
print('Giờ phút giây hiện tại: ',datetime.now().strftime("%H:%M:%S"))