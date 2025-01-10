k=int(input('enter speed:'))
ms_to_kmh= lambda ms: (ms*60*60)//1000
result=ms_to_kmh(k)
print(result) 