# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("members", __name__, url_prefix='/members',
                        static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    return render_template("members/members.html")
