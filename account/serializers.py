from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth.models import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only":True}
                        }

    def validate(self, data):
        email = data['email']
        user_query = User.objects.filter(email=email)
        if user_query.exists():
            raise ValidationError("A user with that email already exists.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

