from .. import database

class Library(database.Model):
    __tablename__ = "libraries"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)

    books = database.relationship(
        "Book",
        back_populates="library",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Library {self.name}>"
