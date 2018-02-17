class flower():
    color = 'RED'
    Raise_prize = 1.5
    no_of_obj = 0
    def __init__(self,name,petals,price):
        self.name = str(name)
        self.petals = int(petals)
        self.price = float(price)
        self.ppp = price/petals
        flower.no_of_obj +=1
    def impo_percent(self):return (1/self.ppp)*100
    def raise_prize(self):return print(self.price*self.Raise_prize)
rose = flower('Rose',7,10)
lily = flower('Lily',8,8)
lotus = flower('Lotus',20,100)
print(rose.__dict__),print(lily.__dict__)
print(lotus.__dict__)
print(rose.impo_percent())
print(lily.impo_percent())
print(lotus.impo_percent())
print(rose.color)
print(rose.raise_prize())
print(lily.raise_prize())
flower.Raise_prize=2.5
print(flower.Raise_prize)
print(rose.raise_prize())
print(lily.raise_prize())
rose.Raise_prize=3.5
print(rose.Raise_prize)
print(lily.Raise_prize)
print(flower.Raise_prize)
print(rose.__dict__)
print(lily.__dict__)
print(flower.__dict__)
print(rose.raise_prize())
print(lily.raise_prize())
print(flower.no_of_obj)
