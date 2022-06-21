from dataclasses import field
from phones_api.models import Phone, User, Number
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'last_name', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, data):
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            last_name=data['last_name']
        )
        Phone.objects.create(surname=user)
        user.set_password(data['password'])
        user.save()
        return user

class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['id', 'phone','number_text']
        read_only_fields = ['id']

class PhoneSerializer(serializers.ModelSerializer):
    numbers = NumberSerializer(many=True)
    author = serializers.StringRelatedField(source='surname')

    class Meta:
        model = Phone
        fields = ['id', 'author', 'surname', 'numbers']
        read_only_fields = ['id']
    
    def create(self, data):
        phone = Phone.objects.create(surname=data['surname'])
        for number in data['numbers']:
            Number.objects.create(phone=phone, number_text=number['text'])
        return phone
