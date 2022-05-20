from transactions import serializers


class TestJokeSerializer:

    def test_valid_joke_serializer(self):
        valid_serializer_data = {
            "text": "My dog used to chase people on a bike a lot. It got so bad I had to take his bike away.",
        }
        serializer = serializers.JokeSerializer(data=valid_serializer_data)
        assert serializer.is_valid(raise_exception=True)
        assert serializer.validated_data["text"] == valid_serializer_data["text"]
