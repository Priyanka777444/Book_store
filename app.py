"""
Priyanka Late Author
1. API Data Retrieval and Storage
January 2026
"""
import requests
import sqlite3
import pandas as pd
from typing import List, Dict


class BookDataAssembler:
    """Assemble book data"""

    def __init__(self, db_name: str = "books.db"):
        """Initilize DB connection"""
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Create books table if not availble already"""
        self.cursor.execute('''
            CREATE table if not exists books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL ,
                author TEXT,
                publication_year INTEGER,
                isbn TEXT
            )
        ''')
        self.conn.commit()
        print("Table created")

    def fetch_book_from_api(self, query: str = "python", limit: int=30) ->List[Dict]:
        """
        Fetch books from open library api
        arguments:
            query : search term for books
            limit : number of books to fecth
        return:
            List of book dictionaries

        """
        url = f"https://openlibrary.org/search.json?q={query}&limit={limit}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            books = []
            for doc in data.get('docs', []):
                book = {
                    'title':doc.get('title', 'unknown'),
                    'author':', '.join(doc.get('author_name',['unknown'])),
                    'publication_year':doc.get('first_publish_year'),
                    'isbn': doc.get('isbn', [None])[0] if doc.get('isbn') else None
                }
                books.append(book)

            print(f"Fetched {len(books)} books from API")
            return books
        except requests.RequestException as e:
            print(F"X API Error: {e}")
            return []

    def insert_books(self, books:List[Dict]):
        """Insert books into db"""
        for book in books:
            self.cursor.execute('''
                INSERT INTO books (title, author, publication_year, isbn)
                VALUES(?, ?, ?, ?)''',(
                    book['title'],
                    book['author'],
                    book['publication_year'],
                    book['isbn']
                ))
            self.conn.commit()
            print(f"Inserted {len(books)} books into database")
    
    def Display_books(self) ->pd.DataFrame:
        """Display books from database"""
        df = pd.read_sql_query("SELECT * FROM books", self.conn)
        print(f"\n{'='*80}")
        print(df.to_string(index = False))
        return df
    def close(self):
        """Closing the connection"""
        self.conn.close()
        print("\n connection closed")

#main execution
if __name__ == "__main__":
    assembler = BookDataAssembler() #initilize assembler

    books = assembler.fetch_book_from_api(query="Machine Learning", limit=30) #fetching books from api

    #inserting into database
    if books:
        assembler.insert_books(books)

    #display results
    df = assembler.Display_books()

    assembler.close() #colsing connection














        
        
