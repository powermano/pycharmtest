class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs): #{'__qualname__': 'Model', '__setattr__': <function Model.__setattr__ at 0x0000000003B37400>, '__init__': <function Model.__init__ at 0x0000000003875D90>, '__getattr__': <function Model.__getattr__ at 0x0000000003881D08>, '__module__': '__main__', 'save': <function Model.save at 0x0000000003F9C2F0>}
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：以及在ModelMetaclass 中的 atrrs
    id = IntegerField('id')  #id:<IntegerField:id>
    name = StringField('username')#name :<StringField:username>
    email = StringField('email')#email : <StringField:email>
    password = StringField('password')#password : <StringField:password>

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')#return a dict {'id':123456, 'name':'Michael','email:'test@orm.org', 'password':'my-pwd'}
# 保存到数据库：
u.save()