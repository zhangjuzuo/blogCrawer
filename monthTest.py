# -*- coding: UTF-8 -*-
from __future__ import print_function
import time

# 开头的文件夹命名
startYear = 2011
startMonth = 11

# 最近的文件夹命名
endYear = int(time.strftime("%Y", time.localtime()))
endMonth = int(time.strftime("%m", time.localtime()))

# 计算月份
length = (endYear - startYear - 1) * 12 + (12 - startMonth + 1) + endMonth

# 文件夹名字拼凑
dirList = []
for i in range(1, length + 1):
    if(startMonth >= 10):
        dirList.append("{0}{1}".format(startYear, startMonth))
    else:
        dirList.append("{0}0{1}".format(startYear, startMonth))
    if (startMonth == 12):
        startMonth = 0
        startYear = startYear + 1
    startMonth = startMonth + 1
print (dirList)
