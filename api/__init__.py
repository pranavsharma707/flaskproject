from api.views import PostListResource,PostResource, UserLogin, UserLogut, UserRegister,docs
from flask_restful import Api, Resource
from api.views import flaskAppInstance,api
from flask_migrate import Migrate




api=Api(flaskAppInstance)

api.add_resource(PostListResource, '/post')
docs.register(PostListResource)
api.add_resource(PostResource, '/posts/<int:post_id>')
docs.register(PostResource)
api.add_resource(UserRegister,'/userregister')
docs.register(UserRegister)
api.add_resource(UserLogin,'/userlogin/<string:email>/<string:password>/')
docs.register(UserLogin)
api.add_resource(UserLogut,'/logout')
docs.register(UserLogut)