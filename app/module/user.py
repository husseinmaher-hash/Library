from .. import database
from sqlalchemy.orm import validates

class User(database.Model):
    __tablename__ = "users"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    library = database.relationship("Library", back_populates="owner", uselist=False)

    @validates('name')
    def validate_name(self, name):
        if not name or len(name.strip()) == 0:
            raise ValueError("user name must be a string ant not empty")
        return name
    

    def __repr__(self):
        return f"<User {self.name}>"
