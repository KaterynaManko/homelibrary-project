from flask import jsonify, request
from app import app, db
from app.models import Author, Book
import json

with app.app_context():
 db.create_all()

@app.route("/api/authors/add", methods=["GET"]) 
def add_authors():
 with app.app_context():    
  with open("authors.json", "r", encoding="utf-8") as f:
   authors = json.load(f)
   for author in authors:
    author = Author(name_surname = author['name_surname'], year_of_birth = author['year_of_birth'])
    db.session.add(author)
    db.session.commit()  
 return jsonify({'message': 'Authors added!'})

@app.route("/api/authors/", methods=["POST"])
def create_author():
 new_author = Author(name_surname = request.json['name_surname'], year_of_birth = request.json['year_of_birth'])
 db.session.add(new_author)
 db.session.commit() 
 return jsonify({'message': 'New author created!'})

@app.route("/api/authors/", methods=["GET"]) 
def all_authors():
 all_authors = Author.query.all()
 output = []
 for author in all_authors: 
    author_data = {}
    author_data['name_surname'] = author.name_surname
    author_data['year_of_birth'] = author.year_of_birth
    output.append(author_data)
 return jsonify(output) 

@app.route("/api/authors/<name_surname>", methods=["GET"])
def get_author(name_surname):
 author = Author.query.filter_by(name_surname=name_surname).first()
 if not author:
    return jsonify({'message': 'No author found!'})
 author_data = {}
 author_data['name_surname'] = author.name_surname
 author_data['year_of_birth'] = author.year_of_birth
 return jsonify({'author': author_data})

@app.route("/api/authors/<name_surname>", methods=['DELETE'])
def delete_author(name_surname):
 author = Author.query.filter_by(name_surname=name_surname).first()
 if not author:
    return jsonify({'message': 'No author found!'})
 db.session.delete(author)
 db.session.commit()
 return jsonify({'message': 'The author has been deleted!'})

@app.route("/api/books/add", methods=["GET"]) 
def add_books():
 with app.app_context():
  with open("books.json", "r", encoding="utf-8") as f:
   books = json.load(f)
   for book in books:
    book = Book(bookname=book['bookname'], genre=book['genre'], status=book['status'], author_id=book['author_id'])
    db.session.add(book)
    db.session.commit()
 return jsonify({'message': 'Books added!'})

@app.route("/api/books/", methods=["POST"])
def create_book():
 new_book = Book(bookname=request.json['bookname'], genre=request.json['genre'], status=request.json['status'], author_id=request.json['author_id'])
 db.session.add(new_book)
 db.session.commit() 
 return jsonify({'message': 'New book created!'})

@app.route("/api/books/", methods=["GET"]) 
def all_books():
 all_books = Book.query.all()
 output = []
 for book in all_books: 
    book_data = {}
    book_data['bookname'] = book.bookname
    book_data['genre'] = book.genre
    book_data['status'] = book.status
    book_data['author_id'] = book.author_id
    output.append(book_data)
 return jsonify(output)

@app.route("/api/books/<status>", methods=["GET"])
def get_book(status):
 books_by_author_id = Book.query.filter_by(status=status).all()
 output = []
 for book in books_by_author_id:
  book_data = {}
  book_data['bookname'] = book.bookname
  book_data['genre'] = book.genre
  book_data['status'] = book.status
  book_data['author_id'] = book.author_id
  output.append(book_data)
 return jsonify(output) 

@app.route("/api/books/<bookname>", methods=["PUT"])     
def update_book(bookname):
 book = Book.query.filter_by(bookname=bookname).first()
 if not book:
    return jsonify({'message': 'No book found!'})
 book.status = "in stock"
 db.session.commit() 
 return jsonify({'message': 'The status of book changed!'})

@app.route("/api/books/<bookname>", methods=['DELETE'])
def delete_book(bookname):
 book = Book.query.filter_by(bookname=bookname).first()
 if not book:
    return jsonify({'message': 'No book found!'})
 db.session.delete(book)
 db.session.commit()
 return jsonify({'message': 'The book has been deleted!'})

if __name__ =='__main__': 
 app.run(debug=True)