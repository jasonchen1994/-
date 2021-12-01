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
print(f)"""
import sys
f = (x**2 for x in range(1,10))
print(sys.getsizeof(f))
print(f)


