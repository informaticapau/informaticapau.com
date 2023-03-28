import yaml
import os
from flask import Blueprint, render_template, send_from_directory

bp: Blueprint = Blueprint('webrings', __name__, url_prefix='/webrings',
                          static_folder='static', static_url_path='',
                          template_folder='templates')

__config_file: str = os.path.join(os.path.dirname(__file__), 'config',
                                    'webrings.yaml')

def __get_webrings() -> dict:
    
    with open(__config_file, 'r') as f:
            return yaml.safe_load(f)

@bp.route("/")
def index() -> str:
    context: dict = {
        'web_badges': __get_webrings(),
    }
    return render_template('webrings/index.html', **context)

@bp.route('/web_badge')
def web_badge() -> str:
    print(bp.static_folder)
    return send_from_directory(bp.static_folder, 'img/web_badge.gif')
    