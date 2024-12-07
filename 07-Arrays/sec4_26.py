import matplotlib.pyplot as plt
x=[]
y=[]
for i in range(-10,10,1):
    x=x+[i]
for n in x:
    y=y+[n-5]
plt.plot(x,y)
plt.show()