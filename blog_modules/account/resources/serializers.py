from rest_framework import serializers

from blog_modules.account.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'note', 'twitter')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'profile', 'username')

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        profile_serializer = ProfileSerializer(instance=instance.profile,
                                               data=profile)
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def validate(self, attrs):
        validate_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        username = validated_data['username']
        user = User.objects.create_user(username=username)
        user.set_password(validated_data['password'])
        user.save()
        return user
