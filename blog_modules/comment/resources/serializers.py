from rest_framework import serializers

from blog_modules.comment.models import Comment


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


