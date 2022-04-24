from rest_framework import serializers
from .models import Articles, User


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'id',
            'content',
            'is_public',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'author',
        )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            group='subscriber'
        )
        return user

    class Meta:
        model = User
        fields = ("id", "email", "password")
        read_only_fields = ("group",)

