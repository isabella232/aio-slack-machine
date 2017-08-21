from importlib import import_module
import inspect

def import_string(dotted_path):
    """
    Import all Classes from the module specified by
    the dotted_path. If dotted_path is not a module, try
    importing it as a Class instead

    returns: list of classes or list of single class
    """

    try:
        module = import_module(dotted_path)
        return inspect.getmembers(module, predicate=inspect.isclass)
    except ModuleNotFoundError:
        try:
            module_path, class_name = dotted_path.rsplit('.', 1)
            module = import_module(module_path)
            return [(class_name, getattr(module, class_name))]
        except AttributeError:
            msg = "{} doesn't look like a module or class".format(dotted_path)
            raise ImportError(msg)

