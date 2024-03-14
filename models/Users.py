from sqlalchemy import Column, Integer, String
from database import Base,db_session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(200), nullable = False)

    def __init__(self,id = None, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.id = id
        self.password = password

    def __repr__(self):
        return f'<User {self.name!r}>'
    
    def serialize(self):
        return {
            "name": self.name,
            "email": self.email
        }
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    
