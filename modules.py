import os
import imp


class ModuleLibrary(object):
    def _load_modules(self):
        files = os.listdir(self.module_folder)
        for fname in files:
            with open(fname) as f:
                contents = f.read()
                mod = imp.load_source()

    def __init__(self, module_folder=None):
        if not module_folder:
            module_folder = os.path.join("lib", "modules")
        self.module_folder = os.path.abspath(module_folder)
        self._load_modules()

    def reload_modules(self):
        self._load_modules()
