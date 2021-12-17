class komplekssayı():
    def __init__(self,reel,snl): #sınıftan nesne oluşturulduğunda otomatik çağrılan bir metottur. yapıcı metottur.
        self.r=reel
        self.s=snl

    #def __del__(self): #oluşturulan nesneyi siler.
        #print("silindi")

x=komplekssayı(2.0,-3)
print(x.r,x.s)
y=komplekssayı(3.0,-9)
print(y.r,y.s)


class Araba():
    #yapıcı metot ve parametreleri
    def __init__(self,model,renk,motor,kapasite):
        self.model=model
        self.renk=renk
        self.motor=motor
        self.kapasite=kapasite
    #özel str metotu
    def __str__(self): #sınıfın string karşılığını verir
        return "model :{}\nrenk :{}\nmotor :{}\nkapasite :{}".format(self.model,self.renk,self.motor,self.kapasite)
#ana program
#araba sınıfından nesneler türet ve ekrana yaz
kamyon=Araba("BMC","kırmızı",3000,9000)
print(kamyon)
print("--------------------")
taksi=Araba("BMW","sarı",1600,2800)
print(taksi)