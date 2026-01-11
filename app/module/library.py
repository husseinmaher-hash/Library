from sqlalchemy.orm import validates
from .. import database

class Library(database.Model):
    __tablename__ = "libraries"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False, unique=True)
    books = database.relationship("Book", back_populates="library", cascade="all, delete-orphan")

    @validates('name')
    def validate_name(self, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("Library name must be a string ant not empty")
        return name
    

    def __repr__(self):
        return f"<Library {self.name}>"
