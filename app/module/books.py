from datetime import datetime
from .. import database
from sqlalchemy.orm import validates
class Book(database.Model):
    __tablename__ = "books"

    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(200), nullable=False)
    author = database.Column(database.String(100), nullable=False)

    libraryId = database.Column(database.Integer,database.ForeignKey("libraries.id"),nullable=False)


    createdAt = database.Column(database.DateTime, default=datetime.utcnow)

    library = database.relationship("Library", back_populates="books")


    @validates('title')
    def validate_title(self,key, title):
        if not title or len(title.strip()) == 0:
            raise ValueError("Book title cannot be empty")
        return title

    @validates('author')
    def validate_author(self, key,author):
        if not author or len(author.strip()) == 0:
            raise ValueError("Author name cannot be empty")
        return author
    
    def __repr__(self):
        return f"<Book {self.title}>"
