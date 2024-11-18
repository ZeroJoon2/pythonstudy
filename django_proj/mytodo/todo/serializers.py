from rest_framework import serializers
from .models import *

class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','complete','important')

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','description','important')

class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        #fields = ('id','title','description','created', 'complete', 'important')
        fields = '__all__'

# class TodoUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ('title','description','complete','important')