from beverages import Coffee, Chocolate, Tea, Cappuccino, HotBeverage
from random import choice

class CoffeeMachine():
    def __init__(self) -> None:
        self.qtd_beverage = 0
        self.broken_machine = False
        
    def description(self, description = "Just some hot water in a cup.") -> str:
        return description
    
    def repair(self):
        self.broken_machine = False
        self.qtd_beverage = 0
        print("\n\033[0;32mRepaired machine!\033[0;37m\n")
        
    def serve(self, hotBeverage):
                
        if self.qtd_beverage >=10 or self.broken_machine:
            self.broken_machine = True
            raise self.BrokenMachineException
        
        beverages = (hotBeverage, self.EmptyCup())
        chosen_beverage = choice(beverages)
        print(chosen_beverage)
        self.qtd_beverage += 1
        
    class EmptyCup(HotBeverage):
        def __init__(self, name = "empty cup", price = 0.90) -> None:
            super().__init__(name, price)

        def description(self, description = "An empty cup?! Gimme my money back!") -> str:
            return description
        

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            self.message = "\33[0;49;31mThis coffee machine has to be repaired.\033[0;37m"
            super().__init__(self.message)


def test():
    
    coffeeMachine = CoffeeMachine()
    beverages = (Cappuccino(), Coffee(), Tea(), Chocolate())
    
    for i in range(24):
        try:
            coffeeMachine.serve(choice(beverages))
        except CoffeeMachine.BrokenMachineException as ex:
            print(ex)
            coffeeMachine.repair()
        

if __name__ == "__main__":
    test()