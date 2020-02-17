# 恼羞成怒
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳地玩耍---" % self.name)


# 继承Dog
class XiaoTianQuan(Dog):
    def game(self):
        # 父类的self属性可以拿来用
        print("%s 飞到天上去玩耍" % self.name)
        # 调用其他类的game方法
        super().game()
        print("%s 再飞到天上去玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, hashiqi):  # 这里的 形参狗 可以是 对象狗
        print("%s 和 %s 快乐的玩耍" % (self.name,
                                 dog.name))  # dog.name调用dog的name方法

        dog.game()  # 调用方法

# dog = Dog("小狗")
dog = XiaoTianQuan("小狗")
sb = Person("小明")


sb.game_with_dog(dog)
"""
# 同样是输入狗对象，使用狗对象里面的方法，
# 但是前面对狗对象的属于哪个类的划分决定了运行哪些代码 
"""