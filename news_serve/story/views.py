
from flask import Blueprint, render_template
from flask.ext.login import login_required
from models import Story
story_blueprint = Blueprint("store", __name__, url_prefix='/stories',
                        static_folder="../static")


@story_blueprint.route("/")
@login_required
def stories():
    st = Story.query.all()
    return render_template("stories/stories.html", stories=st)

@story_blueprint.route("/<int:id>")
@login_required
def story(id):
    st = Story.query.filter_by(id=id).first_or_404()
    return render_template("stories/story.html", story=st)

