#Write a Python program to triple all numbers of a given list of integers. Use Python map.
n=input("enter the integers:")
n=[1,2,3,4,5,6,7]
result=list(map(lambda x:x*3,n))
print(result)