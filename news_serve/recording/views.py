# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required
from news_serve.app import db
from models import Recording
from news_serve.translation.models import Translation
from news_serve.utils import get_or_create
from forms import RecordForm
recording_blueprint = Blueprint("record", __name__, url_prefix='/recordings',
                        static_folder="../static")


@recording_blueprint.route("/")
@login_required
def recordings():
    return render_template("recordings/recordings.html")

@recording_blueprint.route("/<int:id>", methods=["POST","GET"])
@login_required
def record(id):
    trans = Translation.query.get_or_404(id)
    if trans.ready_to_record == True:
        record = get_or_create(db.session, Recording,translation_id=id,translation=trans,text="")
    form = RecordForm(obj=record)
    form.populate_obj(record)
    if request.method == "POST":
       if request.form.get('submit_button')== "Save":
           flash("Story saved.", 'success')
       db.session.add(st)
       db.session.commit()
    return render_template("recordings/record.html",record=record,translation=translation,form=form)
