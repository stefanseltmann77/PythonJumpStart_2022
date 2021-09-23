import datetime

# dates
current_date = datetime.date.today()
specific_date = datetime.date(year=2019, month=8, day=31)

current_date.year
current_date.month
current_date.day()
current_date.weekday()


# datetime
current_time = datetime.datetime.now()
specific_time = datetime.datetime(year=2019, month=8, day=31,
                                  hour=22, minute=15)
current_time.hour
current_time.minute
current_time.second
current_time.microsecond

# str of the objects lead to unix timestamps
str(specific_date) == '2019-08-31'
str(specific_time) == '2019-08-31 22:15:00'

# subtract a week
current_date - datetime.timedelta(days=7)