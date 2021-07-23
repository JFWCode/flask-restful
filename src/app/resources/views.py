from flask import jsonify
from flask_restful import Resource
from src.utils import data_serialize
from .parsers import parser
from src.app.database.models import Bug as BugModel


class Bugs(Resource):
    def get_filter_data(self, req):
        res = {k: v for k, v in req.items() if v != None}
        return res

    def get(self):
        filter_data = self.get_filter_data(parser.parse_args())

        b_query = BugModel.query.filter_by(**filter_data).all()

        data = data_serialize(b_query)
        return jsonify({'data': data})

    def post(self):
        return {}


class Bug(Resource):
    def get(self, id):
        print(type(id))

        b_query = BugModel.query.get(id)

        data = data_serialize(b_query)
        return jsonify({'data': data})
