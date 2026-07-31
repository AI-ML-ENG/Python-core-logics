import datetime
current_time = datetime.datetime.today()
date=current_time.strftime("%Y %m %d")
print(date)
reverse_date=datetime.datetime.strptime(date,"%Y %m %d")
date1= current_time.date()
print(date1)
time=current_time.time()
print(time)
duration=datetime.timedelta(weeks=25)
future=date1+duration
print(future)
futiure1=date1-duration
print(futiure1)