# 제품 클래스 구현
# 속성 : 제품ID:str 제품이름: str, 제품가격:int, 제조사이름:str
#   정보은닉에 맞춰서 작성. 값을 대입/조회 하는 것은 변수처리 방식을 할 수 있도록 구현.
# 메소드: 전체 정보를 출력하는 메소드
# 메소드 : setter-4개, getter-4개. 전체정보 출력하는 메소드-1개

class Products:
    def __init__(self, id, name, price, maker):
        #  Attribute 를 외부에서 접근하지 못하게 막는다. => self.__변수명
        self.__id = id
        self.__name = name
        self.__price = price
        self.__maker = maker

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def maker(self):
        return self.__maker
    
    @maker.setter
    def maker(self, maker):
        self.__maker = maker


    def print_info(self):
        print(f"제품ID : {self.__id}, 제품이름: {self.__name}, 제품가격: {self.__price}, 제조사이름: {self.__maker}")
    

    