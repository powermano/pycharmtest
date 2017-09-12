#super() test
class room:
      def __init__(self,area=120,usedfor='sleep'):
          self.area = area
          self.usedfor = usedfor

      def display(self):
         print("this is my house area=%s usedfor=%s " %(self.area, self.usedfor))

class babyroom(room):
     def __init__(self,area=60,usedfor='son',wallcolor='green'):
         super().__init__(area,usedfor) ##same to room.__init__(20,'doctor')
         self.wallcolr = wallcolor

     def display(self):
         super().display()
         print("babyroom area:%s wallcollor:%s for %s"%(self.area,self.wallcolr,self.usedfor))

class rent:
     def __init__(self,money=1000):
         self.rentmoney = money

     def display(self):
         print("for rent at the price of %s"%self.rentmoney)

class agent(babyroom,rent):
#class agent(rent,babyroom):
     def display(self):
         super().__init__(20,'doctor','yello') #same to babyroom.__init__(20,'doctor','yellow')
         super(agent,self).display()
         print("rent house agent")
         print('first: %s second : %s third: %s '%(self.area, self.usedfor, self.wallcolr))

a = agent()
a.display()
print(agent.mro())
##add more test:test for variable
# this is my house area=20 usedfor=doctor
# babyroom area:20 wallcollor:yello for doctor
# rent house agent
# first: 20 second : doctor third: yello

##the results:
#this is my house
#rent house agent
#[<class '__main__.agent'>, <class '__main__.rent'>, <class '__main__.babyroom'>, <class '__main__.room'>, <class 'object'>]
#如果继承的两个类不是从同一个基类中继承的 ,super()也只会选择一条路走（取决于继承的顺序,例如这里先是rent,那么就
#只会输入rent 的diaplay()，并不会管babyroom的东西，虽然mro()中所有继承的类都有。
class Base(object):
    def __init__(self):
        print('Base init')
class Medium1(Base):
    def __init__(self):
        super(Medium1, self).__init__()
        print('Medium1 init')
class Medium2(Base):
    def __init__(self):
        super(Medium2, self).__init__()
        print('Medium2 init')
class Leaf(Medium1, Medium2):
    def __init__(self):
        super(Leaf, self).__init__()
        print('Leaf init')

leaf=Leaf()
print(Leaf.mro())

# Base init
# Medium2 init
# Medium1 init
# Leaf init
# [<class '__main__.Leaf'>, <class '__main__.Medium1'>, <class '__main__.Medium2'>, <class '__main__.Base'>, <class 'object'>]
#正常的继承情况，多类继承。