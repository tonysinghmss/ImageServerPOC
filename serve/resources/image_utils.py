from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import make_response
import os
import werkzeug
import json

class UploadImage(Resource):
    def __init__(self):
        self.req_parser = RequestParser()
        self.req_parser.add_argument('imgName', required=True, help='Imgae name is mandatory')
        self.req_parser.add_argument('chart', type=werkzeug.FileStorage, location='files', help='Image file is mandataory!')

    def post(self):
        args = self.req_parser.parse_args()
        img = args['chart']
        # print(type(img))
        img_name = args['imgName']
        # print(img_name)
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        img_path = os.path.join(root_dir, 'static', 'images', img_name)
        with open(img_path, 'wb') as fh:
            fh.write(img.read())
        resp = make_response(img_name)
        resp.content_type = 'text/plain'
        return resp

class DownloadImage(Resource):
    def __init__(self):
        self.req_parser = RequestParser()
        self.req_parser.add_argument('imgName', required=True, help='Imgae name is mandatory')
        # self.req_parser.add_argument('chart', type=werkzeug.datastructures.FileStorage, location='files')

    def get(self):
        args = self.req_parser.parse_args()        
        img_name = args['imgName']
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        img_path = os.path.join(root_dir, 'static', 'images', img_name)
        print(img_path)
        with open(img_path, 'rb') as fh:            
            resp = make_response(fh.read())
        resp.content_type = 'image/png'
        return resp
