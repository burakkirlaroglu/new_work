from rest_framework.serializers import ModelSerializer

from blog_modules.account.models import Account
from django.contrib.auth.models import User


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'note', 'twitter')


class UserSerializer(ModelSerializer):
    profile = AccountSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'profile')

    def update(self, instance, validated_data):
        profile = validated_data.pop('profile')
        account_serializer = AccountSerializer(instance=instance.profile,
                                               data=profile)
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()
        return super(UserSerializer, self).update(instance, validated_data)
