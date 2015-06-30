from flask import Blueprint, render_template, request
from flask.ext.login import login_required
from news_serve.story.models import Story
from news_serve.util.models import Language
from news_serve.translation.forms import TranslationForm

translation_blueprint = Blueprint("translate", __name__, url_prefix='/translations',
                      static_folder="../static")


@translation_blueprint.route("/")
@login_required
def translations():
    st = Story.query.filter(Story.ready_to_translate == True).all()
    languages = Language.query.all()
    return render_template("translations/translations.html", stories=st, languages=languages)

@translation_blueprint.route("/<int:id>", methods=["POST","GET"])
@login_required
def translation(id):
    st = Story.query.filter_by(id=id).first_or_404()
    form = TranslationForm(obj=st)
    form.populate_obj(st)
    if request.method == "POST":
       st.text = form.text.data
       if request.form.get('submit_button')== "Save":
           flash("Story saved.", 'success')
       if request.form.get('submit_button')== "Translate":
           flash("Story Ready To Translate.", 'success')
           st.ready_to_translate = True
       db.session.add(st)
       db.session.commit()

    return render_template("translations/translation.html", story=st, form=form)

@translation_blueprint.route("/delegate/<int:story_id>/<int:language_id>")
@login_required
def delegate(story_id, language_id):
    #WUERY for translation with story_id and language
    #if it doesn't exist create it
    return "Functionality TBD"
