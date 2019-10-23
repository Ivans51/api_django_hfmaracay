from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            area=validated_data['area'],
            level=validated_data['level'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = '__all__'
        write_only_fields = ('password',)
        read_only_fields = ('id',)
