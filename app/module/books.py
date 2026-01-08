from datetime import datetime
from .. import database

class Book(database.Model):
    __tablename__ = "books"

    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(200), nullable=False)
    author = database.Column(database.String(100), nullable=False)

    libraryId = database.Column(
        database.Integer,
        database.ForeignKey("libraries.id"),
        nullable=False
    )

    createdAt = database.Column(database.DateTime, default=datetime.utcnow)

    library = database.relationship("Library", back_populates="books")

    def __repr__(self):
        return f"<Book {self.title}>"
