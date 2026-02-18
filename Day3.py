# fibonacci series

# a,b=0,1
# while a<10:
#     print(a, end='')
#     a,b=b,a+b

# tribonacci series

# a,b,c=0,1,1
# while a<30:
#     print(a, end=' ')
#     a,b,c=b,c,a+b+c

# list
# list indices
# list slicing
# list method (append,insert,remove,pop,clear,index,count,sort,reverse)
# list operatios(concentration,repetation,membership)
# mapping(map,filter,reduce)


# list=[1,2,3,4,5]
# print(list[4])
# list slicing makes a new data
# syntax #[start index(included),end index(excluded)]
# print(list[1:4])

# list operator

# concatenation operator(+)
# a=[1,2,3]
# b=[4,5]
# print(a+b)
# realtime usage: E-commerce

# repetition operator(*)
# num=[1,2]
# print(num*5)

# membership operator(in,not-in)
# fruits=["apple","banana","grapes"]
# print("apple" in fruits)
# print("citrus" in fruits)
# print("citrus" not in fruits)

# comparision operator
# list1=[1,2,3]
# list2=[1,2,4]
# print(list1==list2)
# print(list1<list2)
# print(list1>list2)

# a=[1,2,3]
# b=[4,5,6]
# index
# print(a[2])
# print(b[1])
# slicing
# print(a[1:2])
# print(b[:2])
# concatenate
# print(a+b)
# # repetition
# print(a*2,b*3)
# membership
# print(2 in a)
# print(4 in a)
# print(4 not in a)
# print(6 in a)
# comparision
# print(a==b)
# print(a<b)
# print(a>b)

# list methods

# append-> element will be merged at last
# num=[1,2,3]
# num.append(5)
# print(num)

# insert()-> inserts an item at a specific position
# syntax
# insert(index,item)
# num=[1,2,3]
# num.insert(2,4)
# print(num)

# extend()
# a=[1,2]
# b=[3,4]
# a.extend(b)
# print(a)

# remove()
# num=[1,2,3,4,5]
# num.remove(4)
# print(num)

# pop(index)
# num=[10,20,30]
# num.pop(2)
# print(num)

# clear()-> remove all elements
# num=[40,50,60]
# num.clear()
# print(num)

# index()
# num=[10,2,3,4,4]
# print(num.index(3))
# print(num[3])
# count()
# print(num.count(4))

# sort
# a=[1,22,3,44,66]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# reverse
# a=[1,2,3,4,5,6,7]
# a.reverse()
# print(a)

# copy
# a=[1,2,3,4]
# b=[5,3,2,1]
# b=a.copy()
# print(b)

# map(),filter() and list()->functional programming->iteration

# should use it on list
# num=[1,2,3,4]
# result=list(map(lambda x:x*2,num))
# print(result)

# num=[1,2,3,4]
# def func(x):
#     return x*2
# result=list(map(func,num))
# print(result)

# num1=[1,2,3,4,5,6,7,8,9]
# result1=list(filter(lambda x:x%2==0,num1))
# print(result1)

# reduce->convert into a single value->function module
# syntax
# reduce(func,iterable)
# from functools import reduce
# num=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,num)
# print(result)

# seperate odd and even
# num=[1,2,3,4,5,6,7,8,9]
# odd=list(filter(lambda x:x%2!=0,num))
# even=list(filter(lambda x:x%2==0,num))
# print("the odd number is:",odd)
# print("the even number is:",even)

# palindrome-> Avalue that reads the same backward and forward

# 1st method->slicing
# word=input("enter a word:")
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# 2ndmethod->without slicing
word=input("enter your word")
rev=""
for ch in word:
    rev=ch+rev

if word==rev:
    print("palindrome")
else:
    print("not palindrome")