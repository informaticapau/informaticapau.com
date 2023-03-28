from flask import Blueprint, send_from_directory

bp: Blueprint = Blueprint('www', __name__, url_prefix='/',
                          static_folder='static',
                          static_url_path='',
                          template_folder='templates')


@bp.route('/favicon.ico')
def favicon() -> str:
    print(bp.static_folder)
    return send_from_directory(bp.static_folder, 'img/favicon.ico')
