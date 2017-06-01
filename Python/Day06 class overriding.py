class Base:
    a = 1
    def Test(self):
        print 'BaseTest'

class Derived(Base):
    a = 2
    b = 3
    def Test(self):
        Base.Test(self)
        print 'Derived.Print'
        print Base.a, self.a, self.b

t = Derived()
t.Test()