from random import randint, uniform
import datetime


def rand01():
    return uniform(0, 1)


def rand010():
    return uniform(0, 10)


for i in range(10):
    print(rand01(), rand010())    
    
    
def randomDependingOnDate():
    today = datetime.date.today()
    r = today.year * today.month * today.day    
    return randint(0, r)

print(randomDependingOnDate())