#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) 
# the selling price and set max price(change the private attribute max_price).
# Now create an object for the class Computer. 
# Try changing the value of max price and use the sell function to display the updated price. 
# Use a setter function to update the value and again display the price.

class computer:
    def __init__(self,max_price):
        self.max_price= max_price
    def sell(self):
        print(f"The max price is {self.max_price}")
o=computer(250000)
o.sell()
