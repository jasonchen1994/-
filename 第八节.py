"""s1 = r'\'hello word\''
print(s1)
s2='hello'*3
s3 = 'world'
print(s2+s3)
print('ll' in s2)
print('good' in s3)
print(s3[2])
print(s3[2:4])
a,b = 5,10
print('%d*%d=%d'%(a,b,a*b))
print('{0}*{1}={2}'.format(a,b,a*b))
print(f'{a}*{b}={a*b}')
list1=[1,2,3,5,100]
print(list1)
print(len(list1))
print(list1[1])
for index in range(len(list1),0,-1):
    print(index)
for emp in list1:
    print(emp)
list1=[1,2,3,5,100]
list1.append(100)
print(list1)
list1.insert(1,400)
print(list1)
if 3 in list1:
    list1.remove(3)
print(list1)
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)
"""
"""
list=['apple','macbook','iphone']
list1=[1,2,3,5,100,]
list1+=[23,45,21,54]
list2=list1[1:5]
print(list2)
print(list2[:])
print(list1[::-1])
list3=sorted(list2,reverse=True)
list4=sorted(list,key=len)
print(list3)
print(list4)

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
import sys


f=[x for x in range(1,10)]
print(f)
f=[x+y for x in 'ABCED' for y in '12345']
print(f)
f = [x**2 for x in range(1,1000)]
print(sys.getsizeof(f))
print(f)
import sys
f = (x**2 for x in range(1,10))
print(sys.getsizeof(f))
print(f)

def foo():
    print ('hello')
    while True:
        res=yield 4
        print ('res:',res)
g=foo()
print (next(g))
print ('*'*20)
print (next(g))
t = ('chen_jason','94',True,'hhhh')
print(t)
print(t[1])
print(t[0])
peson =list(t)
print(peson)
peson[0] = 'chen'
print(peson)
fruits = ('manago','orange','banana')
fruits_tuple =tuple(fruits)
print(fruits_tuple)

set1 ={1,2,3,5,5,8}
for key in set1:
    print('the key is:%d'%key)
print(set1)
print('length:',len(set1))

set2 = set(range(1,10))
set3 = set(set1)
print(set2,set3)
# set4 = {num for num in range(1,100) if num %3 ==0 or num%5 ==0}
f = [num for num in range(1,100) if num %3 ==0 or num%5 ==0]
# print(set4)
print(f)
set1.add(4)
set1.update([10,20])
print(set1)
set1.discard(3)
if 4 in set1:
    set1.remove(4)
print(set1)
print(set2)
print(set2.pop())
print(set2)
print(set2&set1)
print(set1|set2)
print(set1-set2)
print(set1<=set2)
#   【】列表 （）元组 元素不可更改
# {}集合
"""
t=('221',22,'2323')
p=list(t)
print(p)
# 创建字典的字面量语法
# 创建字典的构造器语法
# 通过zip函数将两个序列压成字典
# 创建字典的推导式语法
# 通过键可以获取字典中对应的值
# 对字典中所有键值对进行遍历
"""scores ={'chen':23,'yuanf':24,'renj':35}
print(f'{scores}')
items1 = dict(one =1,two=2,three=3)
itmes2 = dict(zip(['a','b','c'],'123'))
itmes3={num:num**2 for num in range(1,10)}
print(itmes3,itmes2,items1)
for key in scores:
    print(f'{key}:{scores[key]}')
# 更新字典中的元素
scores['yuanf'] = 65
scores['renj'] = 71
scores.update(冷面=67, 方启鹤=85)
print(scores)
scores ={'chen':23,'yuanf':24,'renj':35}
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('武则天', 60))
print(scores)
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('骆昊', 100))
print(scores)
"""
"""
import os
import time
def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content=content[1:]+content[0]

if __name__ == '__main__':
  main()
"""
content = '北京欢迎你为你开天辟地…………'
print(content[1:])
print(content[0])

import random


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
        print(code)
    return code
print(generate_code())


def _getsuffix (filename,has_dot=False):
    pos = filename.rfind('.')
    if 0<pos<len(filename)-1:
        index=pos if has_dot else  pos+1
        return filename[index:]
    else:
        return ''

abc = input('woshi :')
s = abc.rfind('e')
print(s)


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
print(get_suffix('rar.exe'))
