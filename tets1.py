#encoding=utf-8
import os
import time
from Day6.Class4 import Rectangel

print("--定义一个函数，调用另外一个文件的函数-----------")
rect4=Rectangel(5,9)
print(rect4.caculate_all_length())

print("--格式化输出当前时间，年月日时分秒-----------")
print(time.strftime("%Y-%m-%d %H:%M:%S"))

print("--输出当前文件路径-----------")
adress1=os.getcwd()
print(adress1)

print("--列出当前文件夹路径下所有文件-----------")
print(os.listdir(adress1))

print("--新添加的注释-----------")

print("--新添加的注释-----------")