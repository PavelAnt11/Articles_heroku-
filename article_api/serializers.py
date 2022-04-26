from rest_framework import serializers
from .models import Articles, User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


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
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):

        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            group='subscriber'
        )
        return user

    class Meta:
        model = User
        fields = ("id", "email", "password", "password2")
        read_only_fields = ("group",)
