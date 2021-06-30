class person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def name(self):
        return f'{self.firstname} {self.lastname}'


class Employee(person):
    def __init__(self, first, last, emp_id):
        super().__init__(first, last)
        # self.firstname = first
        # self.lastname = last
        self.employee_id = emp_id
    # def employee_name(self):
    #     return f'{self.firstname} {self.lastname}'




class Rectangle:
    sides = 4
    all_sides_equal = False
    oppsite_side_equal = True
    type = 'rectangle'

    def area(self):
        length = int(input('Enter Length:  '))
        width = int(input('Enter Width:  '))
        return (length * width)
class square(Rectangle):
    all_sides_equal = True
    type = 'square'
    def area(self):
        side = int(input('Enter Side:  '))
        return (side ** 2)
    


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return ('blah blah')


class Dog(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def speak(self):
        return ('bow bow')


class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)

    def speak(self):
        return ('meow meow')

snow = Dog('snow', 'mammal', 'white')
oscar = Cat('oscar', 'mammal', 'gray')

print(snow.speak())    #bow bow
print(oscar.speak())   #meow meow


class Robot:

    def __init__(self, name, model_no, creator):
        self.name = name
        self.model_no = model_no
        self.creator = creator

    def walk(self):
        return 'I am walking using my wheels'

    def charge(self):
        return 'I am charging'


class Dog:

    def __init__(self, height, weight, species=None):
        self.species = species
        self.height = height
        self.weight = weight

    def eat(self):
        return "I'm eating"

    def sleep(self):
        return "I'm sleeping"

    def walk(self):
        return "I'm walking with my legs"


class RoboDog(Robot, Dog):

    def __init__(self, name, model_no, creator, height, weight):
        Robot.__init__(self, name, model_no, creator)
        Dog.__init__(self, height, weight)


Pika = RoboDog('Pika', 'rd-t1', 'Robo-Labs', '2', '5')

print(Pika.walk())      #I am walking using my wheels
print(Pika.sleep())     #I'm sleeping
print(Pika.eat())       #I'm eating
print(Pika.charge())    #I am charging

# Dog.walk(Pika)  


class Book:
    
    def __init__(self, name, author, publisher):
        self.name = name
        self.author = author
        self.publisher = publisher

    def book_details(self):
        return f'{self.name} by {self.author} from {self.publisher}'


class Chapter:

    def __init__(self, title, chap_num, name, author, publisher):
        self.title = title
        self.chap_num = chap_num
        # using composition
        self.book_obj = Book(name, author, publisher)

    def chapter_details(self):
        return f'Chapter {self.chap_num}: {self.title}, is taken from {self.book_obj.book_details()}'


# Chapter obj:
first_chap = Chapter('Composition', 1, 'Best Book', 'RD', 'RD-pubs')

print(first_chap.chapter_details())

# accessing class Book properties and methods using Chapter  Class object
print(first_chap.book_obj.author)
print(first_chap.book_obj.book_details())







