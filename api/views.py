from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from flask_apispec import use_kwargs
from api.config import db
from api.models import Post,Register
from api.schema import post_schema
from flask_restful import Api, Resource
from flask import Flask, app ,request
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS
from app import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from flask import Flask, jsonify, request, session
 
api=Api(flaskAppInstance)

flaskAppInstance.config['SECRET_KEY'] = 'cairocoders-ednalan'

flaskAppInstance.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)

CORS(flaskAppInstance)

flaskAppInstance.config.update({
    'APISPEC_SPEC': APISpec(
        title='Flask Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/'  # URI to access UI of API Doc
})

docs=FlaskApiSpec(flaskAppInstance)

class PostListResource(MethodResource,Resource):
    def get(self):
        if 'email' in session:
           posts = Post.query.all()
           return post_schema.dump(posts,many=True)
        else:
            return "please login"
        # return {'hello': posts}
    
    
    @use_kwargs({'title':fields.Str(),'content':fields.Str()})
    def post(self,**kwargs):
        # print(request.json['title'])
        if 'email' in session:
            new_post = Post(
                titles=request.json['title'],
                content=request.json['content']
            )
            db.session.add(new_post)
            db.session.commit()
            return post_schema.dump(new_post)
        else:
            return "please login"

# api.add_resource(PostListResource, '/post')
# docs.register(PostListResource)


class PostResource(MethodResource,Resource):
    def get(self, post_id):
        if 'email' in session:
            print(session)
            post = Post.query.get_or_404(post_id)
            return post_schema.dump(post)
        else:
            return "please login"

    
    @use_kwargs({'titles':fields.Str(),'content':fields.Str()})
    def patch(self, post_id,**kwargs):
        if 'email' in session:
            post = Post.query.get_or_404(post_id)

            if 'titles' in request.json:
                post.title = request.json['title']
            if 'content' in request.json:
                post.content = request.json['content']

            db.session.commit()
            return post_schema.dump(post)
        else:
            return 'please login'

    def delete(self, post_id):
        if 'email' in session:
            post = Post.query.get_or_404(post_id)
            db.session.delete(post)
            db.session.commit()
            return '', 204
        else:
            return 'please login'


class UserRegister(MethodResource,Resource):
    @use_kwargs({'email':fields.Str(),'password':fields.Str(),'first_name':fields.Str(),'last_name':fields.Str()})
    def post(self,**kwargs):
        user=Register.query.filter_by(email=request.json['email']).first()
        if user:
            return jsonify({'message' : 'please choose a unique email'})
        else:
            password=generate_password_hash(request.json['password'])
            user_register=Register(email=request.json['email'],
            password=password,first_name=request.json['first_name'],
            last_name=request.json['last_name'])
            db.session.add(user_register)
            db.session.commit()
            return "user registered successfully"

class UserLogin(MethodResource,Resource):
    def get(self,email,password):
        if 'email' in session:
            return jsonify({'message' : 'user already login'})
        else:
            user=Register.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password,password):
                    session['email']=email
                    return 'user login successfully'
                else:
                    return "invalid password"
            else:
                return 'invalid user'

class UserLogut(MethodResource,Resource):
     def get(self,**kwargs):
          if 'email' in session:
              session.pop('email', None) 
              return jsonify({'message' : 'You successfully logged out'})
          else:
             return jsonify({'message' : 'loggin'})

    

# api.add_resource(PostResource, '/posts/<int:post_id>')
# docs.register(PostResource)