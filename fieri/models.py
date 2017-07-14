from sqlalchemy import Column, Integer, String
from fieri.database import Base

# class User(Base):
#     __tablename__ = 'users'
#     email = Column(String(120), primary_key=True)
#     name = Column(String(60))

#     def __init__(self, email=None, name=None):
#         self.email = email
#         self.name = name

#     def __repr__(self):
#         return '<User %r %r>' % (self.email, self.name)