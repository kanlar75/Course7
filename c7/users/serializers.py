from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from users.validators import ChatIdValidator


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        validators = [ChatIdValidator(field='chat_id'), ]
