
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_required
from models import Story
from news_serve.app import db
from .forms import StoryForm
from news_serve.utils import get_or_create
from sqlalchemy.sql.expression import ClauseElement

story_blueprint = Blueprint("store", __name__, url_prefix='/stories',
                        static_folder="../staticmethod")


@story_blueprint.route("/", methods=["POST", "GET"])
@login_required
def stories():
    if request.method == "GET":
        st = Story.query.all()
        return render_template("stories/stories.html", stories=st)
    else:
        return redirect(url_for('.new_story'))


@story_blueprint.route("/<int:id>", methods=["POST","GET"])
@login_required
def story(id):
    st = Story.query.filter_by(id=id).first_or_404()
    temp_st = Story()
    temp_st.title = str(st.title)
    temp_st.slug = str(st.slug)
    print st.title
    print "is the title before POST"
    form = StoryForm(obj=st)
    form.populate_obj(st)
    if request.method == "POST":
       print temp_st.title
       print "is temp_st.title"
       st.text = form.text.data
       st.title = temp_st.title
       st.slug = temp_st.slug
       print st.title
       print "is the title after POST"
       if request.form.get('submit_button')== "Save":
           flash("Story saved.", 'success')
       if request.form.get('submit_button')== "Translate":
           flash("Story Ready To Translate.", 'success')
           st.ready_to_translate = True
       db.session.add(st)
       db.session.commit()

    return render_template("stories/story.html", story=st, form=form)

@story_blueprint.route("/new_story", methods=["POST", "GET"])
@login_required
def new_story():
    print "entering new_story"
    form = StoryForm()
    if request.method == "GET":
        return render_template("stories/new_story.html", form=form)
    else:
        st = get_or_create(db.session, Story, title=form.title.data)[0]
        print "debug:"
        print "get_or_create returned", st
        print form.text.data
        print form.title.data
        st.text = form.text.data
        st.title = form.title.data
        st.slug = form.slug.data
        print StoryForm
        db.session.add(st)
        db.session.commit()
        return redirect(url_for('.stories'))
