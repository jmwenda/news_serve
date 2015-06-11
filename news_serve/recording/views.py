# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("record", __name__, url_prefix='/recordings',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def recordings():
    return render_template("recordings/recordings.html")
