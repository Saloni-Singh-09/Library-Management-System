# Library Management System

I created this project to move away from manual record-keeping. It is a command-line tool built with Python that handles book entries, issuance tracking, and data storage without needing a complex database.

---

### Core Logic
Instead of just writing a simple script, I used Object-Oriented Programming (OOP) to make the code modular. 
- The system uses a 'Book' class to define properties.
- A 'LibraryManager' handles the backend operations like adding and listing books.
- Data is synced with a local text file so that information stays saved even after the program closes.

---

### Key Capabilities
1. Dynamic Inventory: Add books anytime while the program is running.
2. Status Tracking: Instantly see if a book is Available or Issued.
3. Persistent Storage: All records are automatically updated in books.txt.

---

### Project Files
- main.py: Contains the full application logic and menu.
- books.txt: Stores all the library data in plain text format.

---

### How to Run
Make sure you have Python installed. Just download the files, open your terminal in that folder, and type:
python main.py

Created by Saloni Singh
