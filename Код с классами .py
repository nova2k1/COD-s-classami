class CustomException1(BaseException):
    pass

class CustomException2(BaseException):
    pass

class CustomException3(BaseException):
    pass

class MyClass:
    def method1(self):
        try:
            # код метода
            if some_condition:
                raise CustomException1("Ошибка метода 1")
            # остальной код метода
        except CustomException1 as e:
            print("Обработка исключения:", e)

    def method2(self):
        try:
            # код метода
            if some_condition:
                raise CustomException2("Ошибка метода 2")
            # остальной код метода
        except CustomException2 as e:
            print("Обработка исключения:", e)

    def method3(self):
        try:
            # код метода
            if some_condition:
                raise CustomException3("Ошибка метода 3")
            # остальной код метода
        except CustomException3 as e:
            print("Обработка исключения:", e)


class AnotherClass:
    def process_object(self, obj):
        try:
            obj.method1()
            obj.method2()
            obj.method3()
        except BaseException as e:
            print("Обработка исключения:", e)


# Пример использования
obj = MyClass()
another_obj = AnotherClass()
another_obj.process_object(obj)