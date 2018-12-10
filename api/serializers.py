from rest_framework import serializers

from api.models import Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    task = serializers.CharField(required=True, max_length=100)
    state = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        
        return instance