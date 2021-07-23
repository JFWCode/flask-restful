from flask.json import JSONEncoder as _JSONEncoder
from datetime import date
import json


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, o)


def data_serialize(query):
    return json.loads(json.dumps(query, cls=JSONEncoder))
