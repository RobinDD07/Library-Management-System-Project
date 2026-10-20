from storage.database import DataHandler

def main():
    db = DataHandler()
    books = db.load_books()

    print(f"\n✅ System loaded successfully! Found {len(books)} book(s) in database.")

    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Overdue Books")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            b_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author: ").strip()
            if b_id and title and author:
                db.add_book(books, b_id, title, author)
            else:
                print("\n❌ All fields are required.")

        elif choice == "2":
            db.display_books(books)

        elif choice == "3":
            b_id = input("Enter Book ID to issue: ").strip()
            if b_id:
                db.issue_book(books, b_id)
            else:
                print("\n❌ Book ID cannot be empty.")

        elif choice == "4":
            b_id = input("Enter Book ID to return: ").strip()
            if b_id:
                db.return_book(books, b_id)
            else:
                print("\n❌ Book ID cannot be empty.")

        elif choice == "5":
            db.check_overdues(books)

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("\n❌ Invalid choice. Select 1 through 6.")

if __name__ == "__main__":
    main()