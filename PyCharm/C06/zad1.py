class Book:
    def __init__(self, title, author, release_year, number_of_pages):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.number_of_pages = number_of_pages

    def cyte(self):
        print("Book info:")
        print("\tTitle: " + self.title)
        print("\tAuthor: " + self.author)
        print("\tRelease year: ", self.release_year)
        print("\tNumber of pages: ", self.number_of_pages)

    def __len__(self):
        return self.number_of_pages


class EBook(Book):
    def __init__(self, title, author, release_year, number_of_pages, format):
        super().__init__(title, author, release_year, number_of_pages)
        self.format = format

    def cyte(self):
        print("Book info:")
        print("\tFormat: " + self.format)
        print("\tTitle: " + self.title)
        print("\tAuthor: " + self.author)
        print("\tRelease year: ", self.release_year)
        print("\tNumber of pages: ", self.number_of_pages)


book1 = Book("Title1", "Autor1", 2000, 345)
book2 = Book("Title2", "Author2", 1996, 654)
print("Book 1: ", book1.title, book1.author, book1.release_year, book1.number_of_pages)
print("Book 2: ", book2.title, book2.author, book2.release_year, book2.number_of_pages)
book2.title = "New Title"
print("Book 2 after changing title : ", book2.title, book2.author, book2.release_year, book2.number_of_pages)
book2.cyte()
print("Book 2 pages num: ", book2.__len__())
ebook1 = EBook("Title3", "Amazon", 2003, 128, "epub")
ebook1.cyte()
