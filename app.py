from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120)) 
    
    def __repr__(self):
        return  f"{self.name}- {self.description}"


@app.get("/")
def home():
     return "Hello Flask"

@app.route('/api/v1/books')
def book():
     books = Book.query.all()
     output = []
     for book in books:
         book_data = {'name': book.name, 'description': book.description}
         output.append(book_data)
     return jsonify(output)

@app.route('/api/v1/book/<id>')
def book_by_id(id):
     book = Book.query.get_or_404(id)
     return jsonify({'name': book.name, 'description': book.description})
     
     
@app.route('/api/v1/books', methods=['POST'])
def create_book():
     book = Book(name=request.json['name'], description=request.json['description'])
     db.session.add(book)
     db.session.commit()
     return jsonify({'id': book.id})

@app.route('/api/v1/book/<id>', methods=['DELETE'])
def delete_book(id):
     book = Book.query.get_or_404(id)
     db.session.delete(book)
     db.session.commit()
     return {"message": "Book deleted successfully!"}

