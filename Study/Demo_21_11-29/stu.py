class Demo:
    def __init__(self, name):
        self.name = name
        print(self.name)

    @classmethod
    def cl(cls, name):
        cls(name)


# d = Demo("chen")
Demo.cl("lkt")
