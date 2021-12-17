from abc import ABC, abstractclassmethod
class soyutSınıf(ABC):
    def __init__(self,value):
        self.value=value
        super().__init__() #alt sınıftaki bir nesneden üst sınıftaki nesneye erişmek için kullanılır.
    @abstractclassmethod
    def islem(self):
        pass


class onekle(soyutSınıf):
    def islem(self):
        return self.value+10


class oncarp(soyutSınıf):
    def islem(self):
        return self.value*10


x=onekle(5)
y=oncarp(5)
print(x.islem())
print(y.islem())

