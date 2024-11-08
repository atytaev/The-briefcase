
from datetime import datetime
from base_models import BaseModel
from sqlalchemy import Integer, String, DateTime, ForeignKey, Column
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Posts(BaseModel):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    comments = relationship('Comment', backref='post')

class Comment(BaseModel):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    author = Column(String)
    content = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())


class Users(UserMixin, BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password_hash = Column(String, nullable=False)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<User %r>' % self.username
