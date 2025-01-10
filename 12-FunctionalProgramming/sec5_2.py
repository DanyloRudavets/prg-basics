from functools import reduce
print(reduce(lambda x,y:x+y,list(filter(lambda x: x%2==0, [2,4,6,3,7,5] ))))