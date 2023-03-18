import os
from flask import Flask


def create_app(test_config: dict = None) -> Flask:
    
    # Create and configure the app
    app: Flask = Flask(__name__, instance_relative_config=True,
                       static_url_path='')
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'flaskapp.db'),
    )
    
    # Routes
    from .routes import bp
    app.register_blueprint(bp)

    # Blueprints
    from .blueprints import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)
    app.add_url_rule('/', endpoint='home.index')
    
        
    # CLI Commands
    from .utils import cli_commands
    for cli in cli_commands:
        app.cli.add_command(cli)

    with app.app_context():
        from .utils import compile_scss
        compile_scss()
        return app
