from flask.cli import AppGroup

cli_commands: list[AppGroup] = []

from .compile_scss import cli, compile_scss
cli_commands.append(cli)