#enpasulation
class mac():
    def __init__(self):
        self.model = "M1 macbook air"
    def sell(self):
        print(f"Selling price: {self.model}")
    def setmax(self,price):
        self.model = price
c = mac()
c.sell()
c.model = "macbook pro m2"
c.sell()

#enpasulation
class mac():
    def __init__(self):
        self.__model = "M1 macbook air"
    def sell(self):
        print(f"Selling price: {self.__model}")
    def setmax(self,price):
        self.__model = price
c = mac()
c.sell()
c.__model = "macbook pro m2"
c.sell()#not change
c.setmax("M2")
c.sell()#change