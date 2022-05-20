from rest_framework import serializers

from transactions import models


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Joke
        fields = ["text", ]
