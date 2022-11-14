import importlib
import pathlib
import os
import inspect
from plugin_abstract import PlugIn


def load_mods(text: str):
    modules = [x.split('.')[0]for x in os.listdir(pathlib.Path() / 'mods')]
    for module_name in modules:
        mod = importlib.import_module(f'mods.{module_name}')
        instances = []
        for _, _cls in inspect.getmembers(mod, inspect.isclass):
            if _cls.__module__.split('.')[-1] == module_name and issubclass(_cls, PlugIn):
                instances.append(_cls())

        for plugin in instances:
            text = plugin.process_text(text)
    print(text)
input('start')
load_mods('test')