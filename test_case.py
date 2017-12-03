#encoding=utf-8
import time
import os


current_dir=os.getcwd()#NEW一个path
print(current_dir)  #查看当前工作目录
print(os.path.split(current_dir)) #将path分割成目录和文件名二元组返回
print("--#获取系统环境变量-----------")
print(os.environ)
print("--#path是自己定义的#path是自己定义的-----------")
print(os.listdir(current_dir))
print("--返回path规范化的绝对路径-----------")
print(os.path.abspath(current_dir))
print("--返回path的目录-----------")
print(os.path.dirname(current_dir))
print("--返回path所指向的文件或者目录最后存取时间-----------")
print(os.path.getatime(current_dir))
print("--返回path所指向的文件或者目录最后修改时间-----------")
print(os.path.getmtime(current_dir))
print("--字符串指示当前使用平台-----------")
print(os.name)
print("-------------")

