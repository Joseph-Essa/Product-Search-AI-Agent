import importlib

def dynamic_import(path: str):
    module_path, attr = path.rsplit('.', 1)
    module = importlib.import_module(f'{module_path}')
    return getattr(module, attr)
