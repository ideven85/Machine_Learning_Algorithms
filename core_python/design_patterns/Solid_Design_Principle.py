import os
import string

"""
Single Responsibility Principle
"""


class Book:
    def __init__(self, name: str, author: str, contents: str):
        self._name = name
        self._author = author
        self._contents = contents

    def replace_text(self, word, replacement):
        if self.word_in_book(word):
            self._contents = self._contents.replace(word.lower(), replacement)

    def word_in_book(self, word):
        return word.lower() in self._contents.lower()

    def __str__(self):
        return self._contents


"""
Formating and Printing Content to output
"""


class BookPrinter:

    def __init__(self, contents):
        self.contents = contents

    def print_to_console(self):
        for t in self.contents.split(" "):
            print(t, end=" ")

    def print_to_media(self, medium_name):
        """
        print to console or given medium
        """
        if medium_name == "console":
            self.print_to_console()


"""
O in SOLID, known as the open-closed principle.
 Simply put, classes should be open for extension but closed for modification. 
In doing so, we stop ourselves from modifying existing code and causing potential new bugs 
in an otherwise happy application.

Of course, the one exception to the rule is when fixing bugs in existing code.
"""


class Guitar:
    def __init__(self, make: str, model: str, volume: int):
        self._make = make
        self._model = model
        self._volume = volume


content = """When we got home we were talking of the old time--which we could all
look back on without despair, for Godalming and Seward are both happily
married. I took the papers from the safe where they had been ever since
our return so long ago. We were struck with the fact, that in all the
mass of material of which the record is composed, there is hardly one
authentic document; nothing but a mass of typewriting, except the later
note-books of Mina and Seward and myself, and Van Helsing’s memorandum.
We could hardly ask any one, even did we Wish to, to accept these as
proofs of so wild a story. Van Helsing summed it all up as he said, with
our boy on his knee"""
book = Book("Fluent_Python", "Deven", content)
book.replace_text("wish", "deven")
print(book)
