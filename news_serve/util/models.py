from news_serve.extensions import bcrypt
from news_serve.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Language(SurrogatePK, Model):
    __tablename__ = 'languages'
    title = Column(db.String(80), unique=True, nullable=False)


    def __init__(self, title="", **kwargs):
        db.Model.__init__(self, title=title, **kwargs)

    def __repr__(self):
        return '<Language({title})>'.format(title=self.title)

class Tag(SurrogatePK, Model):
    __tablename__ = 'tags'
    title = Column(db.String(80), unique=True, nullable=False)

    def __init__(self, title="", **kwargs):
        db.Model.__init__(self, title=title, **kwargs)

    def __repr__(self):
        return '<Tag({title})>'.format(title=self.title)

