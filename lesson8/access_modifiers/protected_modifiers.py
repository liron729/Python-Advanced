from lesson8.access_modifiers.public_modifiers import my_class


class myclass:
    def __init__(self):
        self._protected_variable = "this is a protected variable"

    def _protected_method(self):
        print("this is a protected method")

my_class = myclass()

print(my_class._protected_variable)

my_class._protected_method()