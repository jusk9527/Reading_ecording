# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     单例模式
   Description :
   Author :       jusk?
   date：          2019/11/26
-------------------------------------------------
   Change Activity:
                   2019/11/26:
-------------------------------------------------
"""

# https://zhuanlan.zhihu.com/p/37534850
# python的单例模式
# python的单例模式
## 单例模式是一种常见的软件设计模式，该模式的主要目的，确保某一个类中只有一个实例存在

# python 中使用单例的方法
## 使用模块
## 使用__new__
## 使用装饰器(decorator)
## 使用元类(metaclass)


# --使用模块
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()


from 单例模式 import singleton
print("第一种方式:"+str(id(singleton)==id(singleton)))




# 使用__new__
class Singleton(object):

    _instance = None                    # 默认为None
    def __new__(cls, *args, **kwargs):      # 重写__new__方法，*args,**kwargs 是传入参数
        if not cls._instance:               # 如果默认为None
            cls._instance = super().__new__(cls,*args,**kwargs)        # 则调用super()地址即父类object
        return cls._instance                                            # 如果有就返回那个地址

class MyClass(Singleton):
    a = 1

print("第二种方式:"+str(id(MyClass()==id(MyClass()))))




# -- 使用装饰器
# 将类的实例当成字典的属性

def Singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner



@Singleton
class Cls(object):
    def __init__(self):
        pass

print(id(Cls())==id(Cls()))



# 使用元类
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
   pass


print(MyClass())
print(MyClass())


# <__main__.MyClass object at 0x00000000021BA588>
# <__main__.MyClass object at 0x00000000021BA588>




# 单例创建ORM框架
# class Metaclass(type):
#     def __new__(cls, name, bases, attrs, **kwargs):
#         """
#         :param name: 类型
#         :param bases: 基类
#         :param attrs: 属性字典
#         :param kwargs:
#         :return:
#         """
#         # do something here.
#         print(name)
#         print(bases)
#         print(attrs)
#         print("call Metaclass")
#         return super(Metaclass, cls).__new__(cls, name, bases, attrs, **kwargs)
#
# class User(metaclass=Metaclass):
#     # __metaclass__ = Metaclass # python2支持的方式
#
#     a = "aa"
#     b = "bb"
#     def __init__(self):
#         print("call User")
#
# if __name__ == '__main__':
#     User()




# User
# ()
# {'__module__': '__main__', '__qualname__': 'User', 'a': 'aa', 'b': 'bb', '__init__': <function User.__init__ at 0x10fb67c10>}
# call Metaclass
# call User

# 定义字段属性的基类Field，它的用处主要用于识别类属性中属于字段的那些属性

class Field():
    """
    类型基类
    """
    def __init__(self, db_column, content_type,*args,**kwargs):
        self.db_column = db_column
        self.content_type = content_type

        for key, val in kwargs.items():
            setattr(self, key, val)


        return super().__init__()

    def __str__(self):
        return ("{}".format(self.db_column))

# 整型字段属性
class IntField(Field):
    def __init__(self, db_column="",*args,**kwargs):
        self._value = None # 表的数据
        super().__init__(db_column,content_type="int",*args,**kwargs)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("input should be a Integer")
        self._value = value

    def __get__(self, instance, owner):
        return self._value

# 字符型字段属性
class  CharField(Field):
    def __init__(self, db_column="",*args,**kwargs):
        self._value  = None
        super().__init__(db_column,content_type="string",*args,**kwargs)

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("input should be a String")
        self._value = value



class MetaModel(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        """
        :param name:
        :param bases:
        :param attrs:
        :param kwargs:
        :return:
        """
        fields = {}
        for key, val in attrs.items():
            # 把attrs中与数据库表字段有关的列提取出来
            # 相当于name = CharField(db_column="name",max_length=30)字典的形式
            if isinstance(val, Field):
                fields[key] = val   # value 直接走描述器__get__()

        _meta = {}
        db_table = name.lower()  # 数据表名称默认取小写类名称
        # meta_ = getattr(cls,"Meta",name)
        # print(meta_)
        # loc_db = getattr(meta_,"db_table",None)

        if not db_table:
            _meta['db_table'] = db_table
        else:
            _meta['db_table'] = db_table

        attrs['_meta'] = _meta
        attrs['_fields'] = fields


        # 把原来的attrs相同的属性其实是可以删掉的,节省内存呢

        for key in fields.keys():
            attrs.pop(key)


        # 以上过程相当于对类进行了修改
        return super(MetaModel, cls).__new__(cls, name, bases, attrs, **kwargs)




class Model(metaclass=MetaModel):
    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        return super(Model, self).__init__()

    def save(self):
        fields = []
        values = []
        for key, val in self._fields.items():
            db_column = val.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key) # 字段的值
            values.append(str(value))
        sql = "insert {name} ({field}) values ({value})".format(name=self._meta['db_table'],
                                                             field=','.join(fields),
                                                             value=','.join(values))
        return sql

    def select(self):
        fields = []
        where = []
        for key, val in self._fields.items():
            db_column = val.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            v = getattr(self, key, None)
            if v is not None:
                where.append([key, str(v)])

        sql = 'select {fields} from {name} where {where}'.format(name=self._meta['db_table'],
                                                                 fields=','.join(fields),
                                                                 where=' and '.join(['='.join(x) for x in where]),
                                                                 )
        return sql





class User(Model):
    name = CharField(db_column="name",min_length=20)
    age = IntField(db_column="age")

    class Meta: # 使用内部类来定义数据表的其他属性
        db_table = "xiao"




if __name__ == '__main__':
    user = User(name='seanlee', age=15)
    user.name = 'sean'
    print(user.save())
    print(user.select())

# insert user (name,age) values (sean,15)
# select name,age from user where name=sean and age=15