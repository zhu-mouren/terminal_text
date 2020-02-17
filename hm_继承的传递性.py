class Animal:
    def __init__(self):
        # 子类可以调用父类公有方法和属性，
        # 但不可以直接偷窥父类私有方法和私有属性。
        self.num = 1234567890
        self.__num2 = 1000000

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")
        return "睡觉"


class Dog(Animal):

    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")
    # 覆盖父类的方法（下面的两行）
    # 方法的重写 父类无法满足子类的具体需求，子类中可以编写同名的方法
    # 使用子类时会调用子类中的方法
    def bark(self):
        print("叫的跟神一样")
        # 拓展父类的方法（接下来两行
        # super（）是一个特殊的类
        # 使用 super（）调用原本父类中封装的方法
        """
        另外
        Dog.bark(self)
        """
        Dog.bark(self) # python2.0里面有这个调用父类方法的方法，self一定要写上去
        super().bark() # 会执行子类对应方法，之后再执行下面的代码
        # 子类调用父类方法和父类属性
        print(self.num)
        # 下面这句即执行了sleep函数，又print字符串和sleep函数的返回值"睡觉"
        print("子类方法 %s " % self.sleep())
        print("ertyjh@#$%^&*" + "-" * 30)

# 对父类的方法进行拓展。
# super()是一个特殊的类
dog = XiaoTianQuan
Dog.bark(dog)   # 会调用父类Dog的方法


class Cat(Animal):
    def catch(self):
        print("抓老鼠")


xtq = XiaoTianQuan()
xtq.bark()





