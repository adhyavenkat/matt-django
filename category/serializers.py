from rest_framework import serializers
from .models import Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Category
        fields = ('id', 'name', 'status', 'created_at', 'parent_id')

class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    Category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'category')