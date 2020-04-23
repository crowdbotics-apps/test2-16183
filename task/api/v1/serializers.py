from rest_framework import serializers
from task.models import TaskTransaction, Rating, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class TaskTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTransaction
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
