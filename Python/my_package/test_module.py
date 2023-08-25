
__version__ = "1.0"

def greet(name):
    return f"{name}님 안녕하세요"

def gugudan(dan):
    for i in range(1,10):
        print(f"{dan} X {i} = {dan * i}")
        
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"
