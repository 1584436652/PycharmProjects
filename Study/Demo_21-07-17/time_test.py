"""
继承
"""


class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"早上好！！！my name is {self.name}"


class Son(Father):
    def __init__(self, name, age, like):
        super(Son, self).__init__(name, age)
        self.like = like

    def speak(self):
        return f"早上好！！！my name is {self.name}, i like {self.like}"


son = Son("john", 20, "money")
print(son.speak())
