class Base1:
    @classmethod
    def test_class_methods(cls):
        print("class method of Base1")

    def common(self):
        print("Base1")
class Base2:

    def common(self):
        print("Base2")


class MultiDerived(Base2, Base1 ):
    pass

if __name__ == "__main__":
    m = MultiDerived()
    m.common()

    b1 = Base2()
    b1.common()
    b2 = Base1()
    b2.common()
    Base1.test_class_methods()