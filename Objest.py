#Write a program to create a class with name Student and perform the following tasks - 
#Declare a variable grade Print a sentence inside the class Create an object of class student and see the output

class student:
    grade=7
    print("My grade is",grade)
o= student()


#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a 
#function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two 
#functions to execute them

class intro:
    grade=7
    name="Ranesh Nagar"
    def nesh(self):
        print("My class is",self.grade)
        print("My name is",self.name)
o=intro()
o.nesh()


#Write a program to create a class Parrot and perform the following tasks - 
#Create a class variable species Create a __init__ method that has instance variables - name and age Create 
#instances of class Parrot, passing arguments as well Print Class variable by accessing it Print Instance variables as well
class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return"{} sings {}".format(self.name,song)
        print("The song is",self.song)
o=Parrot("Macow",12)
print(o.name)
print(o.age)
print(o.sing("Bones"))
    


#name and age Create instance methods for this class named sing and dance, making them print a message. Create instances of class Parrot, 
#passing arguments as well Print Class variable by accessing it Print Instance variables as well



    
    
 