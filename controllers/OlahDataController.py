from config.configuration import Configuration

from datetime import datetime


# mysql = MySQL(app())

class OlahDataController(object):
        def __init__(self):
            pass
        def hello(self):
            try:
                return [{"msg":"hello"}]
            except Exception as e:
                # fail response
                return [{"msg":"error "+e}]
        