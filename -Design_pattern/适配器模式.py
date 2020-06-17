# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     适配器模式
   Description :
   Author :       jusk?
   date：          2019/11/26
-------------------------------------------------
   Change Activity:
                   2019/11/26:
-------------------------------------------------
"""
# 手机充电有很多种接口，有typtc的，有原来的，我们能不能有一个接口能支持不同的充电口

# 比如我们


class Computer:
   def __init__(self, name):
       self.name = name
   def __str__(self):
       return 'the {} computer'.format(self.name)
   def execute(self):
       return 'executes a program'


class Synthesizer:
   def __init__(self, name):
       self.name = name

   def __str__(self):
       return 'the {} synthesizer'.format(self.name)

   def play(self):
       return 'is playing an electronic song'


class Human:
   def __init__(self, name):
       self.name = name

   def __str__(self):
       return '{} the human'.format(self.name)

   def speak(self):
       return 'says hello'


class Adapter():
    """
    不使用继承，使用__dict__完成适配
    """
    def __init__(self, obj, adapted_methods):
       self.obj = obj
       self.__dict__.update(adapted_methods)

    def __str__(self):
       return str(self.obj)

def main():
   objects = [Computer('Asus')]
   synth = Synthesizer('moog')
   objects.append(Adapter(synth, dict(execute=synth.play)))
   human = Human('Bob')
   objects.append(Adapter(human, dict(execute=human.speak)))
   for i in objects:
       # 用统一的execute适配不同对象的方法，这样在无需修改源对象的情况下就实现了不同对象方法的适配
       print('{} {}'.format(str(i), i.execute()))

if __name__ == "__main__":
   main()



# the Asus computer executes a program
# the moog synthesizer is playing an electronic song
# Bob the human says hello