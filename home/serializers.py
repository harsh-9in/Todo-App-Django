from rest_framework import serializers
from .models import todo_item

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todo_item
        fields='__all__'