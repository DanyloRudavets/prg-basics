j={"country":"Denmark","gold":2,"silver":4,"bronze":6}
{"country":"Finland","gold":5,"silver":0,"bronze":4}
{"country":"USA","gold":12,"silver":5,"bronze":11}
{"country":"Peru","gold":0,"silver":1,"bronze":7}
import matplotlib.pyplot as plt
import numpy as np
l=list(map(lambda w: (w['gold'] + w['silver']+ w['bronze']), j ))
a=list(map(lambda p: p['country'], j ))
y = np.array(l)
x = np.array(a)

plt.bar(x,y)
plt.show()