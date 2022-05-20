from django.http import Http404
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from transactions import constants
from transactions import models, serializers
from transactions import services


class JokeGetAPIView(views.APIView):
    model_class = models.Joke
    service_class = services.JokeService

    def get(self, request, joke_type=None, *args, **kwargs):
        if joke_type is None:
            joke_type = 'random'
        if joke_type not in models.JokeType:
            return Response({"message": constants.JOKE_DOESNT_MATCH}, status=status.HTTP_400_BAD_REQUEST)
        joke_service = self.service_class(joke_type)
        joke = joke_service.get_joke()
        if joke:
            return Response({"joke": joke}, status=status.HTTP_200_OK)
        else:
            return Response({"message": constants.INTERNAL_SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class JokeAPIView(views.APIView):
    serializer_class = serializers.JokeSerializer
    model_class = models.Joke

    def get_object(self, pk):
        try:
            return self.model_class.objects.get(pk=pk)
        except self.model_class.DoesNotExist:
            raise Http404

    def get_queryset(self):
        return self.model_class.objects.all()

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            serializer = self.serializer_class(self.get_object(pk))
        else:
            serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, *args, **kwargs):
        joke = self.get_object(pk)
        serializer = self.serializer_class(joke, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        joke = self.get_object(pk)
        joke.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
