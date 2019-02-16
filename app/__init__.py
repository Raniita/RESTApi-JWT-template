from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

blueprint = Blueprint('api', __name__)

api = Api(blueprint, 
		  title='Flask restplus api with JWT',
		  version='1.0',
		  description='a boilerplate',
		  authorizations=authorizations
		)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
