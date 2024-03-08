
class PemodelanController(object):
        def __init__(self):
            pass
        def hello(self):
            try:
                return [{"msg":"hello"}]
            except Exception as e:
                # fail response
                return [{"msg":"error "+e}]
        