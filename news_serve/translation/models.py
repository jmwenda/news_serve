from news_serve.extensions import bcrypt
from news_serve.database import (
    Column,
    db,
    Model,
    ReferenceCol,
    relationship,
    SurrogatePK,
)

class Translation(SurrogatePK, Model):
    __tablename__ = 'translations'
    text = Column(db.Text())
    created = Column(db.DateTime())
    modified = Column(db.DateTime())
    lock = Column(db.Boolean())
    ready_to_record = Column(db.Boolean())
    user_id = ReferenceCol('users', nullable=True)
    user = relationship('User', backref='translations')
    story_id = ReferenceCol('stories', nullable=True)
    story = relationship('Story', backref='translations')
    language_id = ReferenceCol('languages', nullable=True)
    language = relationship('Language', backref = 'translations')

    def __init__(self, **kwargs):
        db.Model.__init__(self, **kwargs)

    def __repr__(self):
        return '<Translation({title})>'.format(title=self.story.title)


