from .models import student
from rest_framework import serializers

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['name', 'age', 'contact']
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age =validated_data.get('age', instance.age)
        instance.conctact = validated_data.get('contact', instance.contact) 
        instance.save()
        return instance