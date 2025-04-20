# 📘 Manga Inventory Manager

A lightweight Flask web app for managing a manga inventory system, complete with features to add new manga, search by title or genre, and record manga sales.

---

## 🚀 Features

- 🔍 Search for manga by **title** or **genre**
- ➕ Add new manga to the inventory
- ✏️ Update quantity and details if manga already exists
- 🧾 Record sales of manga and auto-update inventory
- 🏠 Home page navigation with styled interface and manga images

---

## 📂 File Structure

```
project_root/
├── app.py
├── data/
│   └── data.csv
├── static/
│   ├── css/
│   │   └── search.css
│   ├── images/
│   │   ├── One Piece 100.jpg
│   │   ├── Bleach 19.jpg
│   │   └── Naruto 26.jpg
│   └── pages/
│       ├── addmangatoinventory.html
│       ├── searchmanga.html
│       └── mangasold.html
└── main.html
```

---

## 🏠 Home Page

The home page is the main entry point of the Manga Inventory Manager app. It provides quick navigation to all core features and displays a few example manga covers for visual appeal.

### ✨ Features

- Welcoming title and layout
- Images of popular manga (e.g., One Piece, Bleach, Naruto)
- Three primary buttons:
  - **Add Manga to Inventory**
  - **Search for Manga**
  - **Manga Sold**

---

## 📥 Add Manga

Users can add manga by providing the following:
- Title
- Author
- Genre
- Price
- Quantity

### Behavior
- If the manga already exists with `quantity = 0`, it updates the record.
- If the manga exists with `quantity > 0`, it alerts the user.
- If it doesn't exist, it adds the new entry.

---

## 🔍 Search Manga

Search by title via `/search_manga?title=SomeTitle`
Search by genre via `/search_manga_by_genre?genre=Action`

Returns matching manga info in JSON format or an error if not found.

---

## 💸 Record Manga Sold

Submit a manga sale by providing:
- Title
- Quantity sold

### Logic
- Checks if the title exists and quantity is sufficient.
- If sale proceeds and quantity reaches zero, user is prompted to delete the manga.

---

## ⚙️ Backend (Flask)

Routes:
- `GET /search_manga`
- `GET /search_manga_by_genre`
- `POST /add_manga`
- `POST /record_manga_sold`
- `GET /` → Serves `main.html`

CSV file acts as a lightweight database for storing manga information.

---

## 🧪 Example Entry in `data/data.csv`
```
Naruto,Masashi Kishimoto,Action,9.99,15
```

---

## 🖼️ Screenshot Preview (HTML Pages)

- **Home Page**: `main.html` with buttons and manga images.
- **Add Manga**: Form input with validation and logic.
- **Search Manga**: Find manga by genre or title.
- **Manga Sold**: Logic checks for stock before deducting and updates the CSV.

---

## ✅ Requirements

- Python 3+
- Flask

To install Flask:
```bash
pip install flask
```

---

## ▶️ Run the App

```bash
python app.py
```
Then visit `http://localhost:5000` in your browser.

---

## 📌 Future Improvements

- Add delete route for manga entries
- Store data in SQLite or PostgreSQL
- User authentication
- RESTful API design with pagination and filtering

---

## 👨‍💻 Author

Created by Fernando.

