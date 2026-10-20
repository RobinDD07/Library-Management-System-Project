import json
from models.book import Book
from datetime import datetime, timedelta

class DataHandler:
    def __init__(self, filename="library_data.json"):
        self.filename = filename

    def load_books(self):
        books = {}
        # Assumes 'library_data.json' ALREADY exists in your folder
        with open(self.filename, "r") as file:
            data = json.load(file)
            for b_id, b_info in data.items():
                books[b_id] = Book(
                    b_info['book_id'], 
                    b_info['title'], 
                    b_info['author'], 
                    b_info['is_issued']
                )
        return books

    def save_books(self, books):
        """Saves current state back to your JSON file."""
        with open(self.filename, "w") as file:
            data = {b_id: book.to_dict() for b_id, book in books.items()}
            json.dump(data, file, indent=4)

    def add_book(self, books, book_id, title, author):
        if book_id in books:
            print("\n❌ Error: A book with this ID already exists!")
            return
        
        books[book_id] = Book(book_id, title, author)
        self.save_books(books)
        print(f"\n✅ Book '{title}' added successfully!")

    def display_books(self, books):
        if not books:
            print("\n📚 No books available in the collection.")
            return
            
        print("\n--- Current Library Collection ---")
        for book in books.values():
            status = f"Issued (Due: {book.due_date})" if book.is_issued else "Available"
            print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Status: {status}")

    def issue_book(self, books, book_id, loan_days=14):
        if book_id not in books:
            print("\n❌ Error: Book ID not found.")
            return

        book = books[book_id]
        if book.is_issued:
            print(f"\n⚠️ Notice: '{book.title}' is already issued.")
            return

        today = datetime.now()
        due = today + timedelta(days=loan_days)

        book.is_issued = True
        book.issue_date = today.strftime("%Y-%m-%d")
        book.due_date = due.strftime("%Y-%m-%d")

        self.save_books(books)
        print(f"\n✅ Book '{book.title}' issued successfully! Due date: {book.due_date}")

    def return_book(self, books, book_id, daily_fine_rate=5.0):
        if book_id not in books:
            print("\n❌ Error: Book ID not found.")
            return

        book = books[book_id]
        if not book.is_issued:
            print(f"\n⚠️ Notice: '{book.title}' was not checked out.")
            return

        fine = 0.0
        if book.due_date:
            due_dt = datetime.strptime(book.due_date, "%Y-%m-%d")
            today_dt = datetime.now()
            if today_dt > due_dt:
                overdue_days = (today_dt - due_dt).days
                fine = overdue_days * daily_fine_rate

        book.is_issued = False
        book.issue_date = None
        book.due_date = None

        self.save_books(books)
        
        if fine > 0:
            print(f"\n✅ Book '{book.title}' returned. ⚠️ Overdue fine due: ₹{fine:.2f}")
        else:
            print(f"\n✅ Book '{book.title}' returned on time with no fines.")

    def check_overdues(self, books):
        today = datetime.now()
        overdue_found = False

        print("\n--- Overdue Books & Pending Fines ---")
        for book in books.values():
            if book.is_issued and book.due_date:
                due_dt = datetime.strptime(book.due_date, "%Y-%m-%d")
                if today > due_dt:
                    overdue_days = (today - due_dt).days
                    fine = overdue_days * 5.0
                    print(f"ID: {book.book_id} | Title: {book.title} | Due Date: {book.due_date} | Days Late: {overdue_days} | Fine: ₹{fine:.2f}")
                    overdue_found = True

        if not overdue_found:
            print("🎉 No overdue books at this time!")