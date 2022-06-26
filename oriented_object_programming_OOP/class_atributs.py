class A:
    v = 123

    def __int__(self):
        pass


a1 = A()
a2 = A()
A.v = 'alterado'
print(a1.__dict__)
print(a2.__dict__)
print(a1.v)
print(a2.v)
print(A.v)