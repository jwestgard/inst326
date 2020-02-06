#!/usr/bin/env python3

import csv
import sqlite3
import sys

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.year = year
        self.author = author

    def write_to(self, db):
        q = '''INSERT INTO books (title, year, author_id) VALUES (?, ?, ?)'''
        c = db.cursor()
        data = (self.title, self.year, self.author.id)
        c.execute(q, data)


class Author():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def create_in(self, db):
        q = '''SELECT id FROM authors WHERE name=?'''
        c = db.cursor()
        data = (self.name,)
        entry = c.execute(q, data).fetchone()
        if entry is not None:
            self.id = entry[0]
        else:
            self.id = self.write_to(db)

    def write_to(self, db):
        q = '''INSERT INTO authors (name) VALUES (?)'''
        c = db.cursor()
        return c.execute(q, (self.name,)).lastrowid


def create_database():
    setup_books = '''CREATE TABLE books (id INTEGER PRIMARY KEY, 
                                         title TEXT,
                                         year INTEGER, 
                                         author_id INTEGER
                                         )'''
    setup_authors = '''CREATE TABLE authors (id INTEGER UNIQUE PRIMARY KEY,
                                             name TEXT
                                             )'''
    conn = sqlite3.Connection(':memory:')
    cursor = conn.cursor()
    cursor.execute(setup_books)
    cursor.execute(setup_authors)
    conn.commit()
    return conn, cursor


def main():
    filter = tuple([sys.argv[2]])
    db, cursor = create_database()
    with open(sys.argv[1]) as fh:
        for row in csv.reader(fh):
            author = Author(row[2])
            author.create_in(db)
            book = Book(row[1], author, row[3])
            book.write_to(db)
            db.commit()

        join_query = '''SELECT authors.name, books.title, books.year
                        FROM books JOIN authors ON books.author_id=authors.id
                        WHERE authors.name=?'''
        for book in cursor.execute(join_query, filter).fetchall():
            print(book)

if __name__ == "__main__":
    main()
