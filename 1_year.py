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
    print(f"I am {ages} years old,so I have lived for {secondinage} seconds ")

age(1406000000)