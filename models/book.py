class Book:
    def __init__(self, book_id, title, author, is_issued=False, issue_date=None, due_date=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued
        self.issue_date = issue_date  
        self.due_date = due_date    

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued,
            "issue_date": self.issue_date,
            "due_date": self.due_date
        }