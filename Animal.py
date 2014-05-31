class Animal(object):

    """docstring for Animal"""

    def run(self):
        print 'Animal is running...'


class Dog(Animal):

    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'


class Cat(Animal):

    def run(self):
        print 'Cat is running'


def run_twice(animal):
	animal.run()
	animal.run()
dog = Dog()
dog.run()
run_twice(dog)