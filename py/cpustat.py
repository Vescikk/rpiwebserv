from datetime import timedelta
from sys import argv
from time import time

import psutil as psu
NAME = argv[0]

print(timedelta(seconds=time()-psu.boot_time()))
print(psu.cpu_percent(interval=5))
print(psu.cpu_freq())

# def system_info():
#     info = {
#         "Uptime": timedelta(seconds=time()-psu.boot_time())
#     }
#     print(info.items)
# system_info()

