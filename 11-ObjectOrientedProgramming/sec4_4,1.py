from sec4_4 import EBOOK
book1=EBOOK('HArry Potter','J.K. Rowling',300)
EBOOK.book_open(book1)
print(EBOOK.book_status(book1))
EBOOK.page_up(book1)
EBOOK.page_up(book1)
EBOOK.page_up(book1)
print(EBOOK.book_status(book1))
EBOOK.book_close(book1)