class araba: #genel araba tanımı class'da yapılır.
    hiz=0 #her araba 0kmde oluşur
    renk=""#her arabanın rengi farklı
    tekersayisi=4 #her arabanın 4 tekeri var
    def hizlan(self):
        self.hiz=self.hiz+1

x=araba() #özel araba tanımı burada yapılır.(x arabası) #object #bir sinıftan object tanımlamaya instantiation (örenekleme denir.)
print("arabanın hizi",x.hiz)
x.hiz=100
x.hizlan()
print("arabanın hizi",x.hiz)

y=araba() #(y arabası) #object2 #INSTANTIATION
y.hiz=70
y.hizlan()

print("y arabanin hizi",y.hiz)
print("x arabanin hizi",x.hiz)


class araba():
    model="BMW"
    renk="SİYAH"
    silindir=6
    km=100000

kamyon=araba() #INSTANTIATION
taksi=araba() #INSTANTIATION
taksi.model="Renault"
taksi.silindir=4
taksi.km=50000

print(kamyon.model)
print(taksi.km)
print()
print(type(araba))
print(type(kamyon))


