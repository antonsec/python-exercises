class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"Publication: {self.name}\nAuthor: {self.author}\nPage count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f"Publication: {self.name}\nChief Editor: {self.chief_editor}")

magazine = Magazine("Donald Duck", "Aki Hyppää")

book =  Book("Compartment No. 6", "Rosa Liksom", 192)
print ("")
magazine.print_information()
print ("")
book.print_information()