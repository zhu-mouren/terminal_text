class A:

    def test(self):
        print("A test 方法")

    def demo(self):
        print("A demo 方法")

class B:
    def demo(self):
        print("B demo 方法")

    def test(self):
        print("B test 方法")


# 多继承可以让子类对象同时具有多个父亲的属性和方法
# 多继承的注意事项
# 如下所示，同名函数放在前面的优先，也就是后面继承的同名函数没有任何意义
class C(A, B):
    pass

c = C()
c.demo()
c.test()


# 确认C类对象调用方法，object 是所有类的基类
print(C.__mro__)