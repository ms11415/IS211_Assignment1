#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1, Part 2"""


class Book(object):
    """A book."""

    def __init__(self, author="", title=""):
        """Constructor for Book class.

        Args:
            author(str): Author name. Defaults to empty string.
            title(str): Title name. Default to empty string.

        Attributes:
            author(str): Author name.
            title(str): Title name.
        """
        self.author = author
        self.title = title

    def display(self):
        print "\"" + self.author + ", written by " + self.title + "\""

book1 = Book("Of Mice and Men", "John Steinbeck")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book1.display()
book2.display()

