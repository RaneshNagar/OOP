class book:
  def __init__(self, list_of_books, name):
      self.booksList = list_of_books
      self.name = name
      self.lendDict = {}
      
def addBook(self, book):
   self.booksList.append(book)
print(f"{book} has been added to the book list.")

def displayBooks(self):
    print(f"We have the following books in our library: {self.name}")
    for book in self.booksList:
     print(book)
def lendBook(self, user, book):
    if book not in self.booksList:
        print("Sorry, we do not have that book.")
    elif  book in self.lendDict:
        print(f"The book is already being used by {self.lendDict[book]}")
    else:
        self.lendDict[book] = user
        print("Lender-Book database has been updated. You can take the book now.")

