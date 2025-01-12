j=[508,500,512,499,492,511,503,476,501,509]
k=list(filter(lambda x: abs(x-500)>500*0.02, j))
print((len(k)/len(j))*100,'%')