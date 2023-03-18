from flask import Blueprint
from importlib import import_module

def __load_blueprints(modules: list):
    loaded_blueprints: list = []
    for m in modules:
        module = import_module(m, __name__)
        try:
            loaded_blueprints.append(module.bp)
        except:
            print(f"Could not import module: '{m}'!")
    return loaded_blueprints

blueprints: list[Blueprint] = __load_blueprints([
    '.home',
    '.hacking',
    '.social',
])