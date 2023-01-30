#用[]创建list，可以嵌套，逗号分隔，值可以重复,可以混合多种类型的值
list1 = [1,2,'cat','rat',4,5,2,1]
list2 = [[1,2,3,4,5],['cat','rat','bat']]

#取值和切片：用下标（从0开始编号）取值，可以是下表的范围，省略代表到端头，可以是负数（-1表示倒数第一个）
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
