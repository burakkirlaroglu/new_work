from rest_framework import serializers
from blog_modules.post.models import Post


class PostSerializer(serializers.ModelSerializer):
    active_post_count = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "created_date",
            "is_active",
            "active_post_count",
            "modified_by",
            "user_name",
            "slug",
            "media",
            "updated_date",
            "url",)

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


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "media",
            "is_active")

    def validate_title(self, obj):
        if obj == "fenerbahçe":
            raise serializers.ValidationError("title değeri fenerbahçe olamaz")
        return obj

    def validate(self, attrs):
        content = attrs['content']
        if content == "fb":
            raise serializers.ValidationError(
                '{} değeri olamaz'.format(content))
        return attrs
