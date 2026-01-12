from .. import database
from sqlalchemy.orm import validates

class User(database.Model):
    __tablename__ = "users"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    libraryId = database.Column(database.Integer, database.ForeignKey("libraries.id"))
    library = database.relationship("Library", back_populates="users")

    @validates('name')
    def validate_name(self,key, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("user name must be a string ant not empty")
        return name
    

    def __repr__(self):
        return f"<User {self.name}>"
