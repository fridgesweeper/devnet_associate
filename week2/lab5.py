"""
第三方库导入
"""

#第一种导入方式
import yaml.error as eor
#第二种导入方式
#from yaml import error as eor

#列出eor中的所有方法
print(dir(eor))

#分割线
print("\n ********************************** \n")

#eor的文件名字
print(eor.__name__)

#分割线
print("\n ********************************** \n")

#eor的文档
print(eor.__doc__)
