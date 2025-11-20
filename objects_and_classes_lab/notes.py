class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f'The {self.color} {self.brand} is driving.')

    def refuel(self):
        print(f'The {self.color} {self.brand} is refueling with petrol.')


class ElectricCar(Car):
    def __init__(self, color, brand, battery_range: int):
        super().__init__(color, brand)
        self.battery_range = battery_range

    def refuel(self):
        print(f'The {self.color} {self.brand} is charging. Range {self.battery_range}')


pertrol_car = Car('Red', 'Opel')
pertrol_car.drive()
pertrol_car.refuel()

# if we want to specify we will receive int 
# we need to write it in the method
electric_car = ElectricCar('Blue', 'Tesla', 500)
electric_car.drive()
electric_car.refuel()

# methods with __ are dunder methods



class Car1:
    def __init__(self, model):
        self.model = model

    def start(self):
        return print(f'{self.model} is starting!')
    

class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        car.start()

my_car = Car1('Mercedes')
driver = Driver('Ivelina')

driver.drive(my_car)



class User():
    def __init__(self, username):
        self.username = username
        self.friends = []
        self.photos = []
        self.posts = []

    def add_friend(self, friend):
        self.friends.append(friend)
        print(f'{self.username} added {friend.username} as friend')

    
    def create_post(self, content):
        post = Post(self, content)
        self.posts.append(post)

    def view_post(self):
        print(f"\n{self.username}'s Posts")
        for post in self.posts:
            print(f' - {post.content} by {post.author.username}')


class Post():
    def __init__(self, author, content):
        self.author = author
        self.content = content
        

def important(func):
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        return '[IMPORTANT] ' + content
    return wrapper


class AdminUser(User):

    @important
    def prepare_important_content(self, content):
        return content
    
    def create_important_post(self, content):
        important_content = self.prepare_important_content(content)
        post = Post(self, important_content)
        self.posts.append(post)
        print(f'{self.username} posted in IMPORTANT message {important_content}')

ivelina = User('Ivelina')
radi = AdminUser('Radi')

ivelina.add_friend(radi)
radi.create_post('System maintanance tonight')
radi.create_important_post('Security allert!')
ivelina.create_post('Hello SoftUni!')

ivelina.view_post()
radi.view_post()