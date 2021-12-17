import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=np.arange(2,11,2)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,color = "red",linewidth = 5,linestyle = "--")

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,color = "red",linewidth = 5,linestyle = "-.")

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,color = "red",linewidth = 5,linestyle = ":")

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,color = "red",marker ="o",markersize=10,markerfacecolor ="black")

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,color = "red",marker ="o",markersize=20,markerfacecolor ="black",markeredgecolor = "yellow",markeredgewidth = 10)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,lw=3,ls ="--")

ax.set_xlim(0,20)
ax.set_ylim(0,50)

plt.show()