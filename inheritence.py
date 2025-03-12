class person:
    def __init__(self,name,idnumber):
        name = name
        idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee (person):
    def __init__(self,name,idnumber,salary,post):
        salary = salary
        post = post
        person.__init__(self,name,idnumber)
o = employee('Rnaesh',230021,1000000000,'CEO') 
o.display()       
        