class Intern():
    def __init__(self, name = "My name? I’m nobody, an intern, I have no name.") -> None:
        self.name = name
    
    def __str__(self) -> str:
        return self.name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    def make_coffee(self):
        return self.Coffee()
    
    class Coffee():
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."  


def test_one():
    obj_intern = Intern()
    print(obj_intern.name)
    try: 
        obj_intern.work()
    except Exception as ex:
        print(str(ex))

def test_two():
    obj_intern = Intern("Mark")
    print(obj_intern.name)
    print(obj_intern.make_coffee())



if __name__ == "__main__":
    test_one()
    test_two()