# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     orm
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

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
        # rs = getattr(cls, "Meta")
        # res = getattr(rs, "db_table")
        # for i in attrs:
        #     print(i)
        #     try:
        #         if i["Meta"]:
        #             res = getattr(i["Meta"], )
        #             print(res)
        #     except:
        #         pass
        try:
            # print(attrs["Meta"])
            rs = getattr(attrs["Meta"], "db_table",db_table)
            # print(rs)
            # print(type(rs))


            if rs:
                _meta['db_table'] = rs
            else:
                _meta['db_table'] = db_table
        except:
            pass
        attrs['_meta'] = _meta
        attrs['_fields'] = fields


        # 把原来的attrs相同的属性其实是可以删掉的,节省内存呢

        for key in fields.keys():
            attrs.pop(key)

        # 以上过程相当于对类进行了修改
        return super().__new__(cls, name, bases, attrs, **kwargs)




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
        pass




if __name__ == '__main__':
    user = User(name='seanlee', age=15)
    user.name = 'sean'
    # user.name = 1212

    print(user.save())
    print(user.select())