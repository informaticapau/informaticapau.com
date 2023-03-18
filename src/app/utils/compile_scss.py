import app
import os
import sass
from flask.cli import AppGroup
from app.blueprints import blueprints

cli: AppGroup = AppGroup('scss', short_help="SCSS compilation options.")

def compile_scss(debug: bool = False):
    compile_queue: list[tuple[str,str]] = []
    
    # App files
    scss_folder = os.path.join(os.path.dirname(app.__file__), 'src', 'scss')
    css_folder = os.path.join(os.path.dirname(app.__file__), 'static', 'css')
    compile_queue.append(((scss_folder, css_folder)))
    
    # Blueprints files
    for bp in blueprints:
        scss_folder = os.path.join(os.path.dirname(bp.static_folder), 'src',
                                   'scss')
        if os.path.exists(scss_folder):
            css_folder = os.path.join(bp.static_folder, 'css')
            compile_queue.append(((scss_folder, css_folder)))
    
    for dirs in compile_queue:
        if debug: print(f"[INFO] Compiling files in {dirs[0]} to {dirs[1]}...")
        sass.compile(dirname=dirs, output_style='expanded')
    
    if debug: print("[INFO] '.scss' files compiled.")

@cli.command('compile')
def cli_compile_scss() -> None:
    """Compiles all '.scss' files to '.css'."""
    compile_scss(True)