from datetime import datetime, timedelta
now=datetime.now()
haha=now+timedelta(seconds=5)
print('Thời gian hiện tại: ',datetime.now().strftime("%H:%M:%S"))
print('Thời gian sau khi cộng 5s: ',haha.strftime("%H:%M:%S"))