class CustomException1(BaseException):
    pass

class CustomException2(BaseException):
    pass

class CustomException3(BaseException):
    pass

class MyClass:
    def method1(self):
        try:
        
            if some_condition:
                raise CustomException1("Ошибка метода 1")
            
        except CustomException1 as e:
            print("Обработка исключения:", e)

    def method2(self):
        try:
            
            if some_condition:
                raise CustomException2("Ошибка метода 2")
            
        except CustomException2 as e:
            print("Обработка исключения:", e)

    def method3(self):
        try:
        
            if some_condition:
                raise CustomException3("Ошибка метода 3")
            
        except CustomException3 as e:
            print("Обработка исключения:", e)


class AnotherClass:
    def process_object(self, obj):
        try:
            obj.method1()
            obj.method2()
            obj.method3()
        except BaseException as e:
            print("Обработка исключения:", 
            
obj = MyClass()
another_obj = AnotherClass()
another_obj.process_object(obj)