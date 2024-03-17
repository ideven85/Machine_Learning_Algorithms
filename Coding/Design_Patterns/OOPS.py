class Bird:
    pass

class Duck(Bird):
    """

    """
    def quack(self):
        print("Quack Quack")

def alert(birdie):
    birdie.quack()

def alert_duck(birdie:Duck):
    birdie.quack()

def alert_birdie(birdie:Bird):
    birdie.quack()

class House:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        if new_price > 0 and isinstance(new_price,float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.getter
    def price(self):
        return self._price

    
    @price.deleter
    def price(self):
        del self._price





daffy = Duck()
alert(daffy)
alert_duck(daffy)
alert_birdie(daffy)
house = House(1000)
print(house.price)
house.price = -10
print(house.price)
del house.price
house.price = 200
print(house.price)