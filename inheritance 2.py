class a:
    def f1(self):
        print("baseclass")
class b(a):
    def f2(self):
        print("child class")
class c(a):
    def f3(self):
        print("class 3")
x=b()
x.f1()
x.f2()
x.f3()
    