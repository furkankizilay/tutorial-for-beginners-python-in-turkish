import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,6)
y=np.arange(2,11,2)

plt.plot(x,y,"red")
plt.show()

#aynı düzleme birden fazla grafik çizme

plt.subplot(2,2,1) #ikiye ikili düzlemde birinci grafik
plt.plot(x,y,"blue") #birinci grafiği çizdik

plt.subplot(2,2,2)
plt.plot(y,x,"yellow")

plt.subplot(2,2,3)
plt.plot(y,x,"red")

plt.subplot(2,2,4)
plt.plot(x,x**2,"black")

plt.show() #yukarıdakilerin hepsini kapsar

#------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.arange(2, 11, 2)

fig = plt.figure()
#axes = fig.add_axes([0.1,0.2,0.4,0.6])
#x tarfaından 0.1 yanda başladı, y tarafından 0.2 yukarıda başlasın, 0.4 genişlikte ve 0.6 uzunlukta olsun
#plt.show()

#birden fazla grafik çizme

axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.2,0.3])

axes1.plot(y,x)
axes1.set_xlabel("Outer X")
axes1.set_ylabel("Outer Y")
axes1.set_title("Outher Graph")

axes2.plot(x,y)
axes2.set_xlabel("Inner X")
axes2.set_ylabel("Inner Y")
axes2.set_title("Inner Graph")

plt.show()


#boyut ayarlama
fig=plt.figure(figsize=(4,4))
axes=fig.add_axes([0,0,1,1])
axes.plot(x,y,color="red")
plt.show()