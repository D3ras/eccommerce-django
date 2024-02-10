from rest_framework import serializers
from pooltables.models.customer import CustomUser

class CreateUserSerializer(serializers.ModelSerializer):
    ''' Serializer of creating user '''
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'phone']
  
    def validate_username(self, value):
        # Add any additional username validation logic here
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters long.")
        return value

    def validate_email(self, value):
        # Add any additional email validation logic here
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must end with @example.com.")
        return value

    def validate_phone(self, value):
        # Add any additional username validation logic here
        if len(value) < 10:
            raise serializers.ValidationError("phone number must be atleast 10 intergers long.")
        return value
    def validate_password(self, value):
        # Add any additional password validation logic here
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class MiniUserSerializer(serializers.ModelSerializer):
    ''' Mini version of User Serializer '''
    class Meta:
        model = CustomUser
        fields = ['pk', 'username', 'phone', 'profile_pic']

class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'email', 'username', 'phone',
                  'profile_pic']

class UploadUserPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['profile_pic']
        
 
