
class HotBeverage():
    def __init__(self, name = "hot beverage", price = 0.30) -> None:
        self.name = name
        self.price = price
        
    def description(self, description = "Just some hot water in a cup.") -> str:
        return description
    
    def __str__(self) -> str:
        str =f"name: {self.name}\n" + \
        f"price: {self.price:.2f}\n" + \
        f"description: {self.description()}\n"
        return str    
    

class Coffee(HotBeverage):
    def __init__(self, name = "coffee", price = 0.40) -> None:
        super().__init__(name, price)
    
    def description(self) -> str:
        return super().description('A coffee, to stay awake.')


class Tea(HotBeverage):
    def __init__(self, name = "tea") -> None:
        super().__init__(name)


class Chocolate(HotBeverage):
    def __init__(self, name = "chocolate", price = 0.50) -> None:
        super().__init__(name, price)
    
    def description(self, description = "Chocolate, sweet chocolate...") -> str:
        return description


class Cappuccino(HotBeverage):
    def __init__(self, name = "cappuccino", price = 0.45) -> None:
        super().__init__(name, price)
    
    def description(self, description = "Un po’ di Italia nella sua tazza!") -> str:
        return description


def test():
    hot_beverage = HotBeverage()
    print(hot_beverage)
    
    coffee = Coffee()
    print(coffee)
    
    tea = Tea()
    print(tea)
    
    chocolate = Chocolate()
    print(chocolate)
    
    cappuccino = Cappuccino()
    print(cappuccino)
    


if __name__ == "__main__":
    test()
