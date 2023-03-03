from abc import ABC,abstractmethod
class beagle():
    def _init_(self):
        pass
class boxer():
    def _init_(self):
        pass
class welsh_terrier():
    def _init_(self):
        pass
class Hound(beagle):
    pass
class terrier(welsh_terrier):
    pass
class working(boxer):
    pass
class Dog(Hound,terrier,working,ABC):
    def _init_(self):
        pass
    def nombre(self,nombre):
        self.nombre=nombre      
    
   # def tipo(self):
    #    return "mamifero"

class pet(Dog,ABC):
    def _init_(self):
        pass
    def dog(self, nombre):
        pass
       

#La forma de saber a que método se llama 
# es consultar el MRO o Method Order Resolution.
#  Esta función nos devuelve una tupla con el
#  orden de búsqueda de los métodos. 
# Como era de esperar se empieza en la propia 
# clase y se va subiendo hasta la clase padre,
#  de izquierda a derecha.
#x=pet("hola")
#print (Dog.__mro__)
print (pet.__mro__)