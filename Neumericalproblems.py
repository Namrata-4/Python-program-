# 1. add all odd numbers upto 50 (while loop)
# a = 1
# total = 0
# while (a <= 50):
#     if (a % 2 != 0):
#         total += a
#     a += 1 
# print(total)

# 1. add all odd numbers upto 50 ( whithout using while loop)
# a=1
# total=0
# while(a<=50):
#     total+=a
#     a+=2
# print(total)

#2 print 1st 10 even numbers in reverse order(using while loop)
# number=20
# while(number>0):
#     print(number)
#     number=number-2

#2 print 1st 10 even numbers in reverse order(using for loop)
# for num in range(20,0,-2):
#     print(num)

#3. print odd number (using loop)
# for num in range(1,20,+2):
#     print(num)

#4. max and min element 
# def find(arr):
#     minn,maxx=arr[0],arr[0]
#     for num in arr[1:]:
#         if num<minn:
#             minn=num
#         elif num>maxx:
#             maxx=num
#     return minn,maxx
# array=[1,3,4,2,6,8,4,9]
# minn,maxx=find(array)
# print(maxx,minn)

#5.hcf of two numbers  
num1=int(input())
num2=int(input())
while(num2!=0):
    num1,num2=num2,num1%num2
print(num1)





