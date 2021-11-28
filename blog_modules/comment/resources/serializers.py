from rest_framework import serializers

from blog_modules.comment.models import Comment
from django.contrib.auth.models import User

from blog_modules.post.models import Post


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ('updated_date', 'is_active')

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('something went wrong')

        return attrs

    def get_username(self, obj):
        return obj.user.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommandChildSerializer(serializers.ModelSerializer):
    child = serializers.SerializerMethodField()
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
        # depth = 1 # foreign key'in pk değeri yerine sahip olduğu tüm değerleri gösterir

    def get_child(self, obj):
        if obj.any_children:
            return CommandChildSerializer(obj.children(), many=True).data
