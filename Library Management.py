#------------------------------------------------- Library Management Program ----------------------------------------------------------
#Simple Library Management Program that adds, deletes and searches books from library with persistent storage

import os                                                           #to check if file exists
import json                                                         #to read/write data as json

class Library:                                                      #Class Library created
    
    def __init__(self):                                             #Default Constructor
        #Variables Declared
        self.file_path="books.json"
        self.no_of_books=0
        self.books={}
        self.load_data()

    #Function to save data to json file
    def save_data(self):
        data = {
            "no_of_books": self.no_of_books,
            "books": self.books
        }
        with open(self.file_path, "w") as f:
            json.dump(data, f)

    #Function to load data from json file
    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.no_of_books = data.get("no_of_books", 0)
                self.books = data.get("books", {})
    
    #Function to view the total Number of Books
    def view(self):
        print("\nTotal No. of Books: ",self.no_of_books)            #Prints total number of books present in library
    
    #Function to add books in Library
    def add(self):
        n = int(input("\nEnter the No. of Books to be added: "))
        added = 0
        for _ in range(n):
            name = input(f"Enter Name of Book {_ + 1} : ")
            exists = False
            for a, b in self.books.items():
                if b.lower() == name.lower():
                    exists = True
                    break
            if exists:
                print(f"Error! Book {name} already exists in the Library")
                continue
            new_index = max(self.books.keys(), default=0) + 1
            self.books[new_index] = name
            added += 1
        self.no_of_books += added
        self.save_data()
        print("Books added Successfully!")

    #Function to Delete the given book from Library
    def delete(self):
        x=input("\nEnter the Name of Book to be Deleted: ")
        found=False
        to_delete=None
        for a,b in self.books.items():
            if(b.lower()==x.lower()):
                to_delete=a
                found=True
                break
        if found:
            del self.books[to_delete]
            self.no_of_books-=1
            self.save_data()
            print(f"{x} Deleted Successfully.")
        else:
            print(f"{x} not found in Library.")

    #Function to Search a Book in Library
    def search(self):
        find=input("Enter the Name of the book: ")
        found=False
        index=None
        for a,b in self.books.items():
            if(b.lower()==find.lower()):
                index=a
                found=True
                break
        if found:
            print(f"The Book tagged {find} is at Index: {index}.")
        else:
            print(f"The Book tagged {find} not found in Library.")

    #Function to display all the books of Library
    def display(self):
        print(f"Index : Book Name")
        for a,b in self.books.items():
            print(f"{a} : {b}")

    #Function to check which operation to be performed according to user input
    def operation(self,o):
        if(o==1):
            self.view()
        elif(o==2):
            self.add()
        elif(o==3):
            self.delete()
        elif(o==4):
            self.search()
        elif(o==5):
            self.display()
        else:
            print("Invalid Operation!")
         
        

book=Library()                                                                  #Object for Library class created
a="Welcome to Library Management Program!!"
print(a.center(150))                                                            #String Operation to print the given string at center 
print("\nOperations Available:\n1. View Total No. of Books \n2. Add Book to Library \n3. Delete a Book from Library \n4. Search a Book \n5. Display all the books of library \n ")

#Function to identify which operation to performed
def manage():                               
    try:
        i=int(input("\nEnter the Operation to be performed: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    book.operation(i)
    again=input("\nContinue with Operations(Y/N): ")
    if(again=="Y" or again=="y" or again=="yes"):
        manage()
    else:
        print("\nThank You for Using Library Management Program")
        exit()

manage()

