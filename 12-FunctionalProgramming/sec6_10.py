k={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
import matplotlib.pyplot as plt
import numpy as np

x = np.array(list(map(lambda x: x, k.keys() )))
y = np.array(list(map(lambda x: x, k.values() )))

plt.bar(x,y)
plt.show()