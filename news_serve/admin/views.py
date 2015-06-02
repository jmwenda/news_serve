from flask import Blueprint, render_template, redirect, url_for, request
from flask.ext.login import login_required
from flask.ext.login import current_user
from flask.ext.admin import BaseView, expose, Admin, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import wtf
from news_serve.user.models import User
from news_serve.app import db
from news_serve.public.views import home


blueprint = Blueprint("admin", __name__, url_prefix='/admin',
                        static_folder="../admin")

class MyModelView(ModelView):
	def is_accessible(self):
		return current_user.is_authenticated()

	def _handle_view(self, name, **kwargs):
		if not self.is_accessible():
			return redirect('/')


class MyHomeViewBase(AdminIndexView):
	def is_accessible(self):
		return current_user.is_authenticated()

	def _handle_view(self, name, **kwargs):
		if not self.is_accessible():
			return redirect('/')

class MyHomeView(MyHomeViewBase):
    @expose('/')
    def index(self):
        arg1 = 'Hello'
        return self.render('admin/myhome.html', arg1=arg1)

class MyView(BaseView):
	def is_accessible(self):
		return current_user.is_authenticated()

	def _handle_view(self, name, **kwargs):
		if not self.is_accessible():
			return redirect('/')

class UsersView(MyView):
    @expose('/')
    @login_required
    def index(self):
    	print self.is_accessible()
    	print self.is_authenticated()
    	print User.query.all()
        return self.render('admin/users.html', users=User.query.all())

class CatsView(MyView):
    @expose('/')
    @login_required
    def index(self):
        return self.render('admin/cats.html')
