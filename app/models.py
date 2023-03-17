from app import db

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name_surname = db.Column(db.Text, index=True, unique=True)
   year_of_birth = db.Column(db.Integer)
   books = db.relationship("Book", backref="write", lazy="dynamic")

   def __str__(self):
       return f"<Author {self.name_surname}>"

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   bookname = db.Column(db.String(100))
   genre = db.Column(db.String(100))
   status = db.Column(db.String(100))
   author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

   def __str__(self):
       return f"<Book {self.id} {self.bookname}>"