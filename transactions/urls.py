from django.urls import path

from transactions.views import joke, mathematical

urlpatterns = [
    path("get-joke", joke.JokeGetAPIView.as_view(), name="get-random-joke"),
    path("get-joke/<str:joke_type>", joke.JokeGetAPIView.as_view(), name="get-joke"),
    path("joke", joke.JokeAPIView.as_view(), name="api-joke"),
    path("joke/<int:pk>", joke.JokeAPIView.as_view(), name="get-joke-by-pk"),

    path("mcm", mathematical.MCMAPIView.as_view(), name="get-mcm-from-list"),
    path("plusone", mathematical.PlusOneView.as_view(), name="get-plus-number-1"),
]
