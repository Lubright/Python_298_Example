class A():
    a = True


class B(A):
    b = True

    def __init__(self):
        self.c = 1


obj = B()

print(A.__dict__)
print(B.__dict__)
print(obj.__dict__)
