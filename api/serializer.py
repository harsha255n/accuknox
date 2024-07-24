from rest_framework import serializers
from django.contrib.auth.models import User



class Signup(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class loin_f(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.CharField()
    password=serializers.CharField() 


    
class searchuser(serializers.Serializer):
    username=serializers.CharField()