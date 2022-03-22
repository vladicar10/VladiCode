#list 


from turtle import st


str_list = ['Life', 'Is', 'Beautiful']

print(str_list)
print(str_list[0])

#Tuples

stock1= ('MSTF',95.00, 92)
type(stock1)

tup1= ('Tuple','is','and','immutable','list')
print(tup1[0])

tup1[1:3]

#append remov index

#Dictionary
my_dict={1:'mesft',2:'IT'}

my_dict2={'name':'Aarav',1:[2,4,10]}

#Modyfying dictionaries
my_dict3={1:'London',2:'Madrid'}

my_dict3[2]='Barcelona'

print(my_dict3)


#Class is a bundle of Methods and Atributes


class myclass(object):
    def __init__(self,aaa,bbb):
        self.a =aaa
        self.b =bbb

x= myclass(4.2,3)


print(x.a,x.b)

        
#Inheritance Examples
class Date(object):
    def get_date(self):
        return '2018-02-02'
    
class Time(Date):
    def get_time(self):
        return '09:00:00'
    
dt = Date()
print("Get date form the Date class: ",dt.get_date())

tm = Time()
print("Get time from the time class: ", tm.get_time())
print("Get date from time class by inheriting or calling Date class method: ", tm.get_date())



class Animal(object):
    def __init__(self, name):
        self.name=name
    def eat(self, food):
        print("El %s is eating %s" %(self.name,food))
        
class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s' %(self.name, thing))
        


d = Dog('Rufo')


print(d.eat('Perron'))



