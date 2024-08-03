# class Animal:
#     def __init__(self,species):
#         self.species=species
#     def make_sound(self):
#         pass
# class Mammal(Animal):
#     def __init__(self,species,habitat):
#         super().__init__(species)
#         self.habitat=habitat
#     def feed(self):
#         return "Milk"
# class Dog(Mammal):
#     def __init__ (self,breed,habitat):
#         super(). __init__("dog",habitat)
#         self.breed=breed
#     def make_sound(self):
#         return "woof"
# class GoldenRetriever(Dog):
#     def __init__(self, habitat):
#         super().__init__("Golden Retriever", habitat)

#     def fetch_ball(self):
#         return "Fetching the ball"

# obj = GoldenRetriever("Home")
# print(obj.feed())          
# class A:
#     def method_a(self):
#         return "Method A"
# class B:
#     def method_b(self):
#         return "Method B"            
# class C(A,B):
#     def method_c(self):
#         return "Meethod C"
# obj = C()
# print(obj.method_a())   


# class Shape:
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = int(radius)

#     def calculate_area(self):
#         return int(3.14 * self.radius * self.radius)

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = int(side_length)

#     def calculate_area(self):
#         return int(self.side_length **2)

# obj = Square("9")
# obj1= Circle("3")
# print(obj.calculate_area())
# print(obj1.calculate_area())

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()
# print(dog.make_sound())
def animal_sound(animal):
    return animal.make_sound()
print(animal_sound(dog))











            
    
