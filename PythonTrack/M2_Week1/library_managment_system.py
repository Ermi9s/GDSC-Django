from collections import defaultdict 

class Book:
    def __init__(self):
        self.books = defaultdict(list) # name:[author,ISBN,availiability]
        
    def add_book(self,title,author,ISBN):
        self.books[title].append(author)
        self.books[title].append(ISBN)
        self.books[title].append(True) #default availiability upon addition is True
        

    def isAvailable(self,title):
        return self.books[title][2]
    
    def isPresent(self,title):
        if title in self.books.keys():
            return True
        
    def makeAvailable(self,title):
        if self.isPresent(title):
            self.books[title][2] = True
        else:
            print("The book is not in the list")

    def give(self,title):
        if self.isPresent(title) and self.isAvailable(title):
            self.books[title][2]= False
        else:
            print("Can't borrow this book")
            
    def getInfo(self,title):
        print(f"Name: {title}")
        print(f"Author: {self.books[title][0]}")
        print(f"ISBN: {self.books[title][1]}")
        print("Is availaible") if self.books[title][2] else print("Not availiable")


class User:
    def __init__(self,ID,user_name):
        self.ID = ID
        self.user_name = user_name

    def borrow(self,title):
        self.has_borrowed



    

    



        