def compare(a1,a2):
    c=False
    if len(a1)==len(a2):
        for i in range(len(a1)):
            if a1[i]==a2[i]:
                c=True
    return c
print(compare(["water","book","sky"],["water","book","sky"]))
print(compare([True,False],[True,False,True]))
print(compare([3,2,1]   , [3,2]))
print(compare([5,3,1],   [5,3,1]))