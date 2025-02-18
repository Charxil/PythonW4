import numpy as np
day = 365
hour = 24
hourinyear= day * hour
print(f'There are {hourinyear} hours in a year')
minute = 60 * hour ## for each day
minindecade = minute * day * 10
print(f'There are {minindecade} minutes in a decade')
second = 60 * minute ## for each day
age = 28
secondinage = second * day * age
print(f'I am {age} years old, so I have lived for {secondinage} seconds')


def age(secondsinage):
    ages = secondsinage / (second * day)
    print(f"I am {ages} years old,so I have lived for {secondsinage} seconds ")

age(1406000000)

def comparepoint(a,b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice+=1
            # print(f'Alice is awarded 1 point.')
        elif a[i] < b[i]:
            bob+=1
            # print(f'Bob is awarded 1 point.')
        else:
            print(f'Neither is awarded a point.')
    print(f"Final score: Alice {alice} Bob {bob}")
    return [alice,bob]
result=comparepoint([5,6,7],[3,6,10])
print(result)
result=comparepoint([17,28,30],[99,16,8])
print(result)

def stars(symbol,col):
    # eachrow = ""
    for j in np.arange(col,0,-1):
        eachrow = (symbol +" ")*j
        print(eachrow)
stars('*',7)

def triangle_area(b,h):
    return 0.5*b*h
print(triangle_area(b=2.28,h=3.55))
