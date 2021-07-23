from flask_restful import reqparse

parser = reqparse.RequestParser()

# 添加参数解析
# Look only in the querystring
parser.add_argument('case_run_id', type=int, location='args')
parser.add_argument('case_id', type=int, location='args')
