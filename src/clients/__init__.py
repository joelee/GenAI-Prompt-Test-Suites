import importlib.util as _importlib_util
from os import path

BASE_PATH = path.dirname(path.realpath(__file__))


def import_client(name):
    module_file = f"{BASE_PATH}/{name}.py"
    if not path.isfile(module_file):
        raise FileNotFoundError(f"Cannot find module file for '{name}'")

    spec = _importlib_util.spec_from_file_location(f"{name.title()}Client", module_file)
    module = _importlib_util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main
