from news_serve.extensions import bcrypt
from news_serve.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Story(SurrogatePK, Model):
    __tablename__ = 'stories'
    title = Column(db.String(80), unique=True, nullable=False)
    slug = Column(db.String(80), unique = True, nullable=True)
    text = Column(db.Text())
    airdate = Column(db.DateTime())
    created = Column(db.DateTime())
    modified = Column(db.DateTime())
    lock = Column(db.Boolean())
    ready_to_translate = Column(db.Boolean())
    user_id = ReferenceCol('users', nullable=True)
    user = relationship('User', backref='stories')
    language_id = ReferenceCol('languages', nullable=True)
    language = relationship('Language', backref = 'stories')


    def __init__(self, title, **kwargs):
        db.Model.__init__(self, title=title, **kwargs)

    def __repr__(self):
        return '<Story({title})>'.format(title=self.title)


