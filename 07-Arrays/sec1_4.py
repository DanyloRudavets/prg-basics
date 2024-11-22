###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

a=''
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last',arr[-1])
print("last but one",len(arr)-2)
print('sum',arr[0]+arr[-1])
print("middle", arr[len(arr)//2])
for i in arr:
    a+=str(i) +" "
print(a)
for i in arr:
    print(i,end=' ')