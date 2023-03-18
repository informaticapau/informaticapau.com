import yaml
import os
from flask import Blueprint, render_template

bp: Blueprint = Blueprint('social', __name__, url_prefix='/social',
                          static_folder='static', static_url_path='',
                          template_folder='templates')

bp.cli.help = "Social Networks section's options."

__config_file: str = os.path.join(os.path.dirname(__file__), 'config',
                                    'links.yaml')

def __get_links() -> dict:
    
    with open(__config_file, 'r') as f:
            return yaml.safe_load(f)

@bp.route("/")
def index() -> str:
    context: dict = {
        'links': __get_links(),
    }
    return render_template('social/index.html', **context)

