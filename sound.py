# Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods - (info and make_sound). 
# Create different objects for each class and pass the parameters. Showcase the concept of polymorphism in this program.


class cat:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def info(self):
    print (f"My name is{self.name},And I am {self.age} years old")
  def make_sound(self):
      print("meow")
      
class dog:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def info(self):
    print (f"My name is{self.name},And I am {self.age} years old")
  def make_sound(self):
      print("bark")
o=cat("Bengula",14)
b=dog("Samual",14)
for pet in (o,b):
    pet.info()
    pet.make_sound()
    