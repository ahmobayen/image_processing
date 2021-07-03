from flask_restx import Api

from flask import Blueprint
from .api_direction_detection import api as ns1
from .api_slot_detection import api as ns2

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

api.add_namespace(ns1)
api.add_namespace(ns2)
