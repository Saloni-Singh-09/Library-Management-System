import os

# Files to store data
BOOKS_FILE = "books.txt"
MEMBERS_FILE = "members.txt"

# ==================== BOOK CLASS ====================
class Book:
    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued # True agar book kisi ne li hui hai

    def to_file_string(self):
        return f"{self.book_id},{self.title},{self.author},{self.is_issued}\n"

# ==================== MEMBER CLASS ====================
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def to_file_string(self):
        return f"{self.member_id},{self.name}\n"

# ==================== FILE MANAGER ====================
class FileManager:
    @staticmethod
    def save_books(books):
        with open(BOOKS_FILE, 'w') as f:
            for b in books:
                f.write(b.to_file_string())

    @staticmethod
    def load_books():
        books = []
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        # is_issued string ko boolean mein convert karna
                        status = parts[3] == 'True'
                        books.append(Book(parts[0], parts[1], parts[2], status))
        return books

# ==================== LIBRARY MANAGER ====================
class LibraryManager:
    def __init__(self):
        self.books = FileManager.load_books()

    def add_book(self):
        bid = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        self.books.append(Book(bid, title, author))
        FileManager.save_books(self.books)
        print("Book added successfully!")

    def list_books(self):
        print("\n--- Library Books ---")
        print(f"{'ID':<10} {'Title':<20} {'Author':<20} {'Status':<10}")
        for b in self.books:
            status = "Issued" if b.is_issued else "Available"
            print(f"{b.book_id:<10} {b.title:<20} {b.author:<20} {status:<10}")

    def issue_book(self):
        bid = input("Enter Book ID to issue: ")
        for b in self.books:
            if b.book_id == bid:
                if not b.is_issued:
                    b.is_issued = True
                    FileManager.save_books(self.books)
                    print(f"Book '{b.title}' issued successfully!")
                else:
                    print("Book is already issued.")
                return
        print("Book not found!")

# ==================== MAIN SYSTEM ====================
class LibrarySystem:
    def __init__(self):
        self.mgr = LibraryManager()

    def run(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Add Book")
            print("2. List Books")
            print("3. Issue Book")
            print("4. Exit")
            choice = input("Select Option: ")

            if choice == '1': self.mgr.add_book()
            elif choice == '2': self.mgr.list_books()
            elif choice == '3': self.mgr.issue_book()
            elif choice == '4': break
            else: print("Invalid Choice!")

if __name__ == "__main__":
    LibrarySystem().run()