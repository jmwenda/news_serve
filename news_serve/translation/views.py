from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("translation", __name__, url_prefix='/translations',
                      static_folder="../static")


@blueprint.route("/")
@login_required
def translation():
        return render_template("translations/translations.html")
