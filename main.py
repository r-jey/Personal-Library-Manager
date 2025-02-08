def main():
    # Menu
    menu_choice = 0
    while menu_choice != 5:
        print(
            """\nWelcome to my Library Program!
            [1] Add a new book.
            [2] List all books.
            [3] Search for a book by title.
            [4] Remove a book by title.
            [5] Exit."""
        )
        menu_choice = int(input())
        
        # Add books
        if menu_choice == 1:
            add_books()
            
        # List books
        elif menu_choice == 2:
            list_books()
    
        # Search books
        elif menu_choice == 3:
            search_books()
        
        # Remove books
        elif menu_choice == 4:
            remove_books()
        
        # Exit
        elif menu_choice == 5:
            print("\nGoodbye!")
            
# Library
books = [
    {"title": "Software Book", "author": "Rolando Balito", "year": 2002,},
    {"title": "Computational Science Book", "author": "Edgardo Bunselo", "year": 2004,},
    {"title": "Operation Systems Book", "author": "Eddie Balulos", "year": 2023,}
]

# Add books function
def add_books():
    print("\nAdd the Book!")
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Publication Year: "))
    new_book = {"title": title, "author": author, "year": year,}
    books.append(new_book)
    print("Book Added!")
                
# List books function
def list_books():
    book_num = 0
    for book in books:
        book_num += 1
        print(f"Book #{book_num}\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\n")

# Search books function
def search_books():
    print("\nFind the Book by Title!")
    title = input("Title: ").lower()
    for book in books:
        match = False
        if title in book['title'].lower():
            print("Book(s) Found!\n")
            print(book['title'].title())
            match = True
    if match == False:
        print("Book cannot be found!\n")

# Remove books function
def remove_books():
    print("\nRemove the Book!")
    title = input("Title: ").lower()
    for book in books:
        match = False
        if book['title'].lower() == title:
            confirm = input("Book found! Are you sure you want to remove this book? [Y/N].").lower()
            while confirm != "y" and confirm != "n":
                confirm = input("Book found! Are you sure you want to remove this book? [Y/N].").lower()
            if confirm == "y":
                books.remove(book)
                print("Book Removed!\n")
            elif confirm == "n":
                print("Book Remained!\n")
            match = True
            break
    if match == False:
        print("Book cannot be found!\n")   
        
main()


 



