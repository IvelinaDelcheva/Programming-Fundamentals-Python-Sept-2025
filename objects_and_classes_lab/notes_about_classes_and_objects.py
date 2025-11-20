class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    
    def start_engine(self):
        print(f'The {self.make} {self.model} engine is starting.')

    
    def stop_engine(self):
        print(f'The {self.make} {self.model} engine is stopping.')


car1 = Car('Mercedes', 'S500', 2022)
car2 = Car('BMW', '750', 2021)

print(car1.make)
print(car2.make)

car1.start_engine()
car2.start_engine()

car1.stop_engine()
car2.stop_engine()

# Check for __init__ method 
# Without this method the attributes of the class
# are not initialized automatically

# self takes everything for the obejct and place it
# in the constructor. Selft helps us to work with the attibutes
# of the object of the class


class Person:
    def __init__(self, first_name, last_name, age = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def person_info(self):
        return f'{self.first_name} {self.last_name}, age: {self.age}'
    
    # gives representation of the instance class
    def __repr__(self):
        return f'I am {self.first_name}'
    

ivelina = Person('Ivelina', 'Delcheva', 33)
print(ivelina.person_info())

#  we can change the values in the attribute class
ivelina.age = 34
print(ivelina.age)

# instance methods __init__

#  class attr with 1 underscore -> protected. do not use it 
# outside the class 

#  class attr with 2 underscores -> protected attr
#  this is done so no one can change it. it is private

# look for protected and private attributes

#  to see all atr of the instance and class
print(ivelina.__dict__)


# repr and str 
# representation of the instance class trough __repr__ func
print(ivelina.__repr__)