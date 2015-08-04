# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, flash, request, redirect, url_for
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
        st_record = Recording.query.filter_by(translation_id=trans.id,translation=trans).first_or_404()
    	form = RecordForm(obj=st_record)
   	form.populate_obj(st_record)
    if request.method == "POST":
        st_record.text = form.text.data
        st_record.ready_to_broadcast = form.ready_to_broadcast.data
        if request.form.get('submit_button')== "Save":
            flash("Recording saved.", 'success')
        db.session.add(st_record)
        db.session.commit()
    return render_template("recordings/record.html",record=st_record,translation=trans,form=form)
