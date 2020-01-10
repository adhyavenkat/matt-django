from rest_framework import serializers
from .models import NewsCategoryRelation
from django.contrib.auth.models import User


class MapperCategorySerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = NewsCategoryRelation
        fields = ('id', 'created_at', 'status', 'category_id', 'news_id')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    mapper = serializers.PrimaryKeyRelatedField(many=True, queryset=NewsCategoryRelation.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'mapper')