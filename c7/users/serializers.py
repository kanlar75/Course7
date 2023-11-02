from rest_framework.serializers import ModelSerializer

from users.models import User
from users.validators import ChatIdValidator


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        validators = [ChatIdValidator(field='chat_id'),]
