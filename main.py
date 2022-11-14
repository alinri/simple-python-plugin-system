import importlib
import pathlib
import os
import inspect
from plugin_abstract import PlugIn


def load_mods(text: str):
    mods = [x.split('.')[0]for x in os.listdir(pathlib.Path() / 'mods')]
    for mod_name in mods:
        mod = importlib.import_module(f'mods.{mod_name}')
        instances = []
        for _, obj in inspect.getmembers(mod, inspect.isclass):
            if obj.__module__.split('.')[-1] == mod_name and issubclass(obj, PlugIn):
                instances.append(obj())

        for plugin in instances:
            text = plugin.process_text(text)
    print(text)
input('start')
load_mods('test')