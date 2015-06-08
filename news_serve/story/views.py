# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("story", __name__, url_prefix='/stories',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def stories():
    return render_template("stories/stories.html")
