from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog_modules.favourite.models import Favourite


class FavouriteListCreateSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, attrs):
        queryset = Favourite.objects.filter(post=attrs['post'],
                                            user=attrs['user'])
        if queryset.exists():
            raise serializers.ValidationError('Zaten favori edilmiş')
        return attrs


class FavouriteAPISerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('content',)