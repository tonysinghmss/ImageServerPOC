from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from serve.resources.image_utils import UploadImage
api.add_resource(UploadImage, '/upload')

from serve.resources.image_utils import DownloadImage
api.add_resource(DownloadImage,'/chart')