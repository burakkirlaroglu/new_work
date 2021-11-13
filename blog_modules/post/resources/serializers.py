from rest_framework import serializers
from blog_modules.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    active_post_count = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "created_date",
            "active_post_count",
            "user_name",
            "slug",
            "media",)

    def get_active_post_count(self, obj):
        """Sum of Posts that is_active field True"""
        qs = Post.objects.all().filter(is_active=True).count()
        return qs

    def get_user_name(self, obj):
        return obj.user.username

# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=120)
#     content = serializers.CharField()
#     is_active = serializers.BooleanField()
#     created_date = serializers.DateTimeField()
#     post_count = serializers.SerializerMethodField()
#
#     def get_post_count(self, obj):
#         """Sum of Posts that is_active field True"""
#         qs = Post.objects.all().filter(is_active=True).count()
#         return qs
