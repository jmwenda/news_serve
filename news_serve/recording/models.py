from news_serve.extensions import bcrypt
from news_serve.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Recording(SurrogatePK, Model):
    __tablename__ = 'recordings'
    text = Column(db.Text())
    created = Column(db.DateTime())
    modified = Column(db.DateTime())
    lock = Column(db.Boolean())
    ready_to_broadcast = Column(db.Boolean())
    user_id = ReferenceCol('users', nullable=True)
    user = relationship('User', backref='recordings')
    translation_id= ReferenceCol('translations', nullable=True)
    translation = relationship('Translation', backref='recordings')

    def __init__(self, title, **kwargs):
        db.Model.__init__(self, story=story, **kwargs)

    def __repr__(self):
        return '<Recording({title})>'.format(title=self.story.title)


