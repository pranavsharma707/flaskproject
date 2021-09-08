from api.models import Post
from api.config import ma

class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")
        model = Post

post_schema = PostSchema()
posts_schema = PostSchema(many=True)