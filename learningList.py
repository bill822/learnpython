#列表是基本数据类型，掌握基本操作可为后续学习打下基础
#用[]创建list，可以嵌套，逗号分隔，值可以重复,可以混合多种类型的值
list1 = [1,2,'cat','rat',4,5,2,1]
list2 = [[1,2,3,4,5],['cat','rat','bat']]

#取值和切片：用下标（从0开始编号）取值，可以是下标的范围，省略代表到端头，可以是负数（-1表示倒数第一个）
x1 = list1[1]       #2
x2 = lsit2[1][0]    #'cat'
y1 = list1[1:3]     #[2,'cat']
y2 = list1[3:]      #['rat',4,5,3,2]
#列表长度，列表串接
list3 = [1,2,3,4,5]
len(list3)          #5
list4 = list1+list3 #串接
b1 = 'cat' in list1 #Ture,是否包含在列表中
b2 = 'cat' not in list1  #not in,False
#枚举列表中的值1
for i in range(len(listname1)):   #既可以访问下标，也可以访问列表项的值
  print(listname1[i])             #可以有更多其他操作
#枚举列表中的值2
for i in listname1:               #只能访问列表的值
  print(listname1[i])             #可以有更多其他操
#针对列表值的操作
listname.index(value)           #某个值在列表中第一次出现的位置（下标）
listname.append(value)          #在列表末尾增加值
listname.insert(position,value) #在指定位置插入值
listname.sort()                 #按ASCII码顺序排序，大小写字母顺序位置不同
listname.sort(reverse=True)     #逆序
listname.sort(key=str_lower)    #按字典字母排序
#字符串str，元组tuple，可以看列表，区别在于其值不可变；元组与列表可互相转换
str1 = 'Hello world'
s1 = str1[0]      #s1: H
tuple1 = tuple('cat','rat','bat')   #用（）创建
list1 = list(tuple1)    #tuple 转换成list
tuple1 = tuple（list1） #list转换成tuple
#列表赋值给另一个列表后，改变其中一个，另外一个也会改变。因为列表赋值操作，只增加了引用，没有实际上增加内存拷贝
list5 = list1 
list5[0] = 10   #修改list5的一个值
print(list5)    #[10, 2, 'cat', 'rat', 4, 5, 2, 1]
print(list1)    #[10, 2, 'cat', 'rat', 4, 5, 2, 1]   list1的值也已经被修改
#如果希望有列表的另外一份拷贝，需要引入copy模块
import copy
list6 =copy.copy(list1)
list6[0] = 10
print(list6)    #[10, 2, 'cat', 'rat', 4, 5, 2, 1]
print(list1)    #[1, 2, 'cat', 'rat', 4, 5, 2, 1]   list1的值保持不变
