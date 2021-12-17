import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=np.arange(2,11,2)

fig,ax = plt.subplots(figsize=(8,6))

ax.plot(x,x**2,color = "red",linewidth = 5,linestyle = "--")
plt.show()
