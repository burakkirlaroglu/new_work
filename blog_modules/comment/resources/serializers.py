from rest_framework import serializers

from blog_modules.comment.models import Comment
from django.contrib.auth.models import User

from blog_modules.post.models import Post


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('created',)

    def validate(self, attrs):
        if attrs['parent']:
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('something went wrong')

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CommandListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
        # depth = 1 # foreign key'in pk değeri yerine sahip olduğu tüm değerleri gösterir

    def get_replies(self, obj):
        if obj.any_children:
            return CommandListSerializer(obj.children(), many=True).data


class CommandDeleteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
