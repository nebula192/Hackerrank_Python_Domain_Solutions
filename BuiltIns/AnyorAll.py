'''
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Author    : Ausaf Hussain Akhlaq
Created   : 28 march 2020
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
'''
n = int(input())

arr=list(map(int,input().split()))
print(all(list(map(lambda i:i>0,arr))) & any(list(map(lambda x:str(x)==str(x)[::-1],arr))))
