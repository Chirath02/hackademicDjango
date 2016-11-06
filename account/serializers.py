from django.db.models import Q
from rest_framework.serializers import ModelSerializer, ValidationError, CharField
from django.contrib.auth.models import User


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {"password": {
                                "write_only": True
                            }
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


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise ValidationError("A username is required")
        user = User.object.filter(Q(username=username))
        user = user.exclude(username__isnull=True).exclude(username__iexact='')
        if user.exist() and user.count() ==1:
            user_obj = user
        else:
            raise ValidationError("This username is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")
        data["token"] = "Random token"
        return data
