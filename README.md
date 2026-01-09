# 📚 Book_store (Assignment)

A Python-based data pipeline that fetches book metadata from the Open Library REST API, cleans the data, and stores it in a local SQLite database for persistent storage.

## 🚀 Features
* **API Integration:** Fetches real-time data using the `requests` library.
* **Data Sanitization:** Cleans messy JSON data (handling missing authors or titles).
* **Persistent Storage:** Uses SQLite to store data locally in `books.db`.
* **Data Analysis:** Utilizes `pandas` to display data in a clean tabular format.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `requests`, `sqlite3`, `pandas`
* **Database:** SQLite
* **Type Hinting:** Uses Python `typing` for robust code structure.

## 📂 Project Structure
```text
D:/Internship/
├── app.py             # Main Python logic
├── books.db           # SQLite Database file (Generated after run)
└── README.md          # Project documentation
