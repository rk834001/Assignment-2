class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}"

    def apply_discount(self, discount):
        self.price -= self.price * (discount / 100)

class EBook(Book):
    def __init__(self, title, author, price, book_format):
        super().__init__(title, author, price)
        self.format = book_format

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Format: {self.format}"

# Example usage:
book1 = Book("Python Programming", "John Smith", 29.99)
print("Book Information:")
print(book1.display_info())

ebook1 = EBook("Python Programming (EBook)", "John Smith", 19.99, "PDF")
print("\nEBook Information:")
print(ebook1.display_info())