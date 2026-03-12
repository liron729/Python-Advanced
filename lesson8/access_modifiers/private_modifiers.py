class myclass:
    def __init__(self):
        self.__private_variable = "This is a private variable"

    def __private_method(self):
        print("this is a private method")

my_class = myclass()

print(my_class.__private_variable)

print(my_class.__private_method())