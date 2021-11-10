from rest_framework import serializers
from blog_modules.post.models import Post
from django.utils.timezone import now


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    content = serializers.CharField()
    is_active = serializers.BooleanField()
    created_date = serializers.DateTimeField()
    post_count = serializers.SerializerMethodField()

    def get_post_count(self, obj):
        """Sum of Posts that is_active field True"""
        qs = Post.objects.all().filter(is_active=True).count()
        return qs
