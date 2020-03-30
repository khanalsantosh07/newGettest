from functools import reduce
def add_all(a,b):
    return a+b

num = [1,2,3,4,5,6,7,8,9]

evens = list(filter(lambda n: n%2==0,num))

doubles = list(map(lambda n: n*2,evens))

sum = reduce(lambda a,b: a+b,doubles)
print(doubles)
print(evens)
print(sum)

