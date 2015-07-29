from flask import Blueprint, render_template, flash, request
from flask.ext.login import login_required
from news_serve.app import db
from news_serve.story.models import Story
from news_serve.translation.models import Translation
from news_serve.util.models import Language
from news_serve.utils import get_or_create
from news_serve.translation.forms import TranslationForm
from news_serve.story.forms import StoryForm

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
    return render_template("translations/translation.html", story=st)

@translation_blueprint.route("/delegate/<int:story_id>/<int:language_id>", methods=["POST","GET"])
@login_required
def delegate(story_id, language_id):
    st = Story.query.filter_by(id=story_id).first_or_404()
    language = Language.query.filter_by(id=language_id).first_or_404()
    translation = get_or_create(db.session, Translation,story_id=story_id,story=st,language=language)
    st_translation = Translation.query.filter_by(story_id=story_id,language=language).first_or_404()
    temp_st = Story()
    temp_st.title = str(st.title)
    temp_st.slug = str(st.slug)
    print st.title
    print "is the title before POST"
    form = TranslationForm(obj=st_translation)
    form.populate_obj(st_translation)
    if request.method == "POST":
       print st_translation.story.title
       print "is st_translation.story.title"
       st_translation.text = form.text.data
       if request.form.get('submit_button')== "Save":
           flash("Story saved.", 'success')
       if request.form.get('submit_button')== "Record":
           flash("Story Ready To Record.", 'success')
           st_translation.ready_to_record = True
       db.session.add(st)
       db.session.commit()
    return render_template("translations/delegatetranslation.html", translation=st_translation, form=form)

    #WUERY for translation with story_id and language
    #if it doesn't exist create it
    #return "Functionality TBD"
