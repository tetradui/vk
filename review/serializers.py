from rest_framework.serializers import ModelSerializer

from .models import Comment, Favorite

class CommentSerializer(ModelSerializer): 
    class Meta:
        model = Comment
        exclude = ['user']
        
    def validate(self, attrs):
        super().validate(attrs)
        request = self.context.get("request")
        attrs['user'] = request.user
        return attrs


class FavoriteSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'post']
        read_only_fields = ['user']


# from rest_framework.serializers import ModelSerializer

# from .models import Comment

# class CommentSerilalizer(ModelSerializer):
#     class Meta:
#         model = Comment
#         # fields = 'post', 'body', 'created_at', 'updated_at'
#         exclude = ['user']
        
#     def validate(self, attrs):
#         super().validate(attrs)
#         request = self.context.get('request')
#         attrs['user'] = request.user
#         return attrs