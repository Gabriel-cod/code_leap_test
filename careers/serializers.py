from rest_framework import serializers
from .models import Career


class CareerGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = '__all__'


class CareerPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = ('username', 'title', 'content')


class CareerPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = ('title', 'content')
