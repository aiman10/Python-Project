import importlib


class Loader():
    @staticmethod
    def load(file):
        return importlib.import_module(file)