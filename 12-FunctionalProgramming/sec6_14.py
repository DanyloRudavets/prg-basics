print((len(list(filter(lambda x: abs(x-500)>500*0.02, [508,500,512,499,492,511,503,476,501,509])))/len([508,500,512,499,492,511,503,476,501,509]))*100,'%')