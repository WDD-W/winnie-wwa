import time
timea = "1660672266"
trx_time = time.localtime(int(timea))
dt = time.strftime('%Y-%m-%d %H:%M:%S',trx_time)
print(dt)