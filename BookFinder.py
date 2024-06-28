import copy

def bookSearch(booklist : list, bookSearchInput : list):
    booksearch = []
    searchGenre = bookSearchInput[1].capitalize()
    for book in booklist:
        if bookSearchInput[0].lower() in book[searchGenre].lower():
            booksearch.append(copy.deepcopy(book))
    return booksearch
#Searches for the specific book/author by checking if the key "book"/"author" value contains the search term. 
def addBook():
    userInput = input("Please enter in the author, book name and the year it was published, seperated by a comma: ").split(",")
    with open("ListOfBooks.txt","a") as r:
        r.write(f"{userInput[0].title()}:{userInput[1].title()}:{userInput[2]}")
        r.close()
    print(f"Successfully added {userInput}")
#Splits the userinput into a list then opens the txt file and appends the line with the proper format.
def helper():
    userInput = input("""What command do you need help with:
Add
Remove
Search
                      """).lower()
    if userInput == "add":
                  print(""""This command asks for the author, book name, and year. 
In the format as followed:author,book name,year
It then adds the book to the database.""")
    elif userInput == "remove":
        print("Removes a book based off of the format:author,book name,year")
    elif userInput == "search":
        print("""Type a book name and it'll return a list of results that match your search.""")

def removeBook(booklist):
    userInput = input("Please enter in the author, book name and the year it was published, seperated by a comma: ").split(",")
    for book in booklist:
        if userInput[0].lower() in book["Author"].lower() and userInput[1].lower() in book["Book"].lower():
            booklist.remove(book)
            return booklist
    print("Sorry, this book is already out of stock.")
#Checks if the book is in the dictionary before removing it, if its not in the dictionary it is assumed that the book is out of stock.
def updateTxt(booklist):
    line = ""
    with open("ListOfBooks.txt","w") as wr:
        for book in booklist:
            for key in book:
                if key == "Year":
                    line += str(book[key])
                    continue
                print(book[key])
                line += str(book[key]) + ":"
            wr.write(line)
            wr.close()
    print("List successfully updated")
#Updates the booklist by rewriting the values through the updated dictionary
def bookCounter(booklist):
    print(f"Total stock: {len(booklist)}")
    lsd = {}
    authorsL = {}
    for book in booklist:
        if book["Book"] not in lsd:
            lsd[book["Book"]] = 0
        if book["Author"] not in authorsL:
            authorsL[book["Author"]] = 0
        lsd[book["Book"]] += 1
        authorsL[book["Author"]] += 1
#Counts the books by checking if the bookname and book author are in the dictionary, if not, it gets added.                
    print(f"Current stock of books by name:\n{lsd}\n\n Current stock of books by Author:\n{authorsL}")
def menu():
    print("""Add: Add a book
Remove: Remove a book
Search: Search for a book
Help: Help manual for the commands
Count: Count the amount of books in stock
""")
    userInput = input("What would you like to do today? ").lower()
    if "add" in userInput:
        addBook()
    elif "remove" in userInput:
        removeBook(booklist)
        updateTxt(booklist)
    elif "search" in userInput:
        bookSearchInput = input("\nEnter the name of the thing you're searching for, and if you're searching for a book or author, seperate by commas. ").split(",")
        booksearchL = bookSearch(booklist, bookSearchInput)
        if len(booksearchL) == 0:
            print("Sorry, this book is out of stock.")
        else:
            previousBooks = []
            for i in range(len(booksearchL)):
                for key,value in booksearchL[i].items():
                    if key not in previousBooks or value not in previousBooks:
                        previousBooks.append(key)
                        previousBooks.append(value)
                        print(f"{key}: {value}")
                        if key == "Year":
                            print("-------")                    
    elif "help" in userInput:
        helper()
    elif "count" in userInput:
        bookCounter(booklist)


if __name__ == "__main__":
    dictionary = {}
    booklist = []
    with open('ListOfBooks.txt','r') as b:
        for line in b:
            (authors,books,year) = line.split(":")
            dictionary["Author"] = authors
            dictionary["Book"] = books
            dictionary["Year"] = int(year)
            booklist.append(copy.deepcopy(dictionary)) 
    menu()
#Reads the txt file and splits the file into authors,books and year, then appends those values to a dictionary, which then gets added to a list.