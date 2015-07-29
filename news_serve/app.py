# -*- coding: utf-8 -*-
'''The app module, containing the app factory function.'''
from flask import Flask, render_template

from news_serve.settings import ProdConfig
from news_serve.assets import assets
from news_serve.extensions import (
    bcrypt,
    cache,
    db,
    login_manager,
    migrate,
    debug_toolbar,
)
from news_serve import public, user, admin, story, translation, recording
from flask.ext.admin.contrib.sqla import ModelView
from .admin.views import CatsView, MyModelView, MyHomeView
from flask.ext.admin import Admin
from news_serve.user.models import User
from news_serve.story.models import Story
from news_serve.util.models import Language, Tag
from news_serve.translation.models import Translation
from news_serve.recording.models import Recording



def create_app(config_object=ProdConfig):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)

    # flask-admin
    amin = Admin(app,index_view=MyHomeView())
    amin.add_view(MyModelView(User, db.session))
    amin.add_view(CatsView(name='Cats'))
    amin.add_view(MyModelView(Story, db.session))
    amin.add_view(MyModelView(Translation, db.session))
    amin.add_view(MyModelView(Recording, db.session))
    amin.add_view(MyModelView(Language, db.session))
    amin.add_view(MyModelView(Tag, db.session))
    return None
    import pdb; pdb.set_trace()  # XXX BREAKPOINT


def register_blueprints(app):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(story.views.story_blueprint)
    app.register_blueprint(recording.views.recording_blueprint)
    app.register_blueprint(translation.views.translation_blueprint)
    return None


def register_errorhandlers(app):
    def render_error(error):
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
