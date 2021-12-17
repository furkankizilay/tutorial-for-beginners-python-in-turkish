import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=np.arange(2,11,2)

fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(8,6))

axes[0].plot(x,y,color="red")
axes[0].set_title("First Axes")
axes[1].plot(x,x**0.5,color="purple")
axes[1].set_title("Second Axes")
plt.tight_layout()
plt.show()

fig.savefig("Figure1.png") #bu figür bir png dosayasın dönüştürüldü
fig.savefig("Figure1.pdf")

#--------------------------------
fig,axes = plt.subplots(figsize=(8,6))

axes.plot(x,x**0.5,label = "X Karekök",color = "red")
axes.plot(x,x**2,label = "X Kare",color = "blue")
axes.plot(x,x**3,label = "X Küp",color = "#9f7adf")
axes.legend()
plt.show()







