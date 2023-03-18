from flask import Blueprint, render_template, send_from_directory

bp: Blueprint = Blueprint('hacking', __name__, url_prefix='/hacking', 
                          static_folder='static', static_url_path='',
                          template_folder='templates')

@bp.route("/")
def index() -> str:
    return render_template('hacking/index.html')