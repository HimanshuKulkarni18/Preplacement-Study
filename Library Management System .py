class Book:
    def __init__(self, book_id, title, author, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"{self.book_id} | {self.title} | {self.author} | Copies: {self.copies}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __str__(self):
        return f"{self.member_id} | {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.issued_books = {}

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        copies = int(input("Enter number of copies: "))

        if book_id in self.books:
            self.books[book_id].copies += copies
        else:
            self.books[book_id] = Book(book_id, title, author, copies)

        print("Book added successfully.")

    def add_member(self):
        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")

        if member_id in self.members:
            print("Member already exists.")
        else:
            self.members[member_id] = Member(member_id, name)
            print("Member added successfully.")

    def issue_book(self):
        book_id = input("Enter book ID to issue: ")
        member_id = input("Enter member ID: ")

        if member_id not in self.members:
            print("Member not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        if self.books[book_id].copies <= 0:
            print("No copies available.")
            return

        self.books[book_id].copies -= 1
        self.issued_books.setdefault(member_id, []).append(book_id)
        print("Book issued successfully.")

    def return_book(self):
        book_id = input("Enter book ID to return: ")
        member_id = input("Enter member ID: ")

        if member_id not in self.issued_books or book_id not in self.issued_books[member_id]:
            print("This book was not issued to this member.")
            return

        self.issued_books[member_id].remove(book_id)
        self.books[book_id].copies += 1
        print("Book returned successfully.")

    def show_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            print(book)

    def show_members(self):
        if not self.members:
            print("No members registered.")
            return
        for member in self.members.values():
            print(member)

    def show_issued_books(self):
        if not self.issued_books:
            print("No books issued.")
            return

        for member_id, book_list in self.issued_books.items():
            member_name = self.members[member_id].name
            print(f"Member: {member_name} ({member_id})")
            for book_id in book_list:
                book = self.books[book_id]
                print(f"  - {book.title} by {book.author}")


def menu():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Show All Members")
        print("7. Show Issued Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.add_member()
        elif choice == "3":
            library.issue_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.show_books()
        elif choice == "6":
            library.show_members()
        elif choice == "7":
            library.show_issued_books()
        elif choice == "8":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


menu()