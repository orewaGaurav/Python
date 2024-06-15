from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self): #Abstract method
        pass
    def show(self): #concrete method
        print("concrete method")
#my = Father()

class child(Father):
    def disp(self):
        print("Defining Abstract Method")
c =child()
c.disp()
c.show() 
print(type(c))
print(id(c))
print(dir(c))
print(str(c))
print(type(c))
print(type(child))
print(isinstance(c,child))
print(isinstance(c,Father))