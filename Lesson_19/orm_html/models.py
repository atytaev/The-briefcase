from datetime import datetime
from base_models import BaseModel
from sqlalchemy import Integer, String, DateTime, ForeignKey, Column
from sqlalchemy.orm import relationship

class Posts(BaseModel):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # comments = relationship('Comment', backref='post')

class Comment(BaseModel):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    author = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)