import pytest
from django_mock_queries.query import MockSet

from transactions import models, serializers
from transactions.views import joke

"""
START FIXTURES
"""


@pytest.fixture
def chuck_joke():
    return models.Joke(
        id=1,
        text="a king cobra once bit Chuck Norris... after 5 days of terrible pain... the snake died"
    )


@pytest.fixture
def chuck_joke_updated():
    return models.Joke(
        id=1,
        text="Updated Joke"
    )


@pytest.fixture
def jokes_queryset():
    qs = MockSet(
        models.Joke(text="My dog used to chase people on a bike a lot. It got so bad I had to take his bike away."),
        models.Joke(text="a king cobra once bit Chuck Norris... after 5 days of terrible pain... the snake died")
    )
    return qs


"""
END FIXTURES
"""


class TestJokeGetAPIView:

    def test_get_random_joke(self, client):
        response = client.get("/api/get-joke")
        assert response.status_code == 200
        assert "joke" in response.json()

    def test_type_doesnt_match(self, client):
        response = client.get("/api/get-joke/any")
        assert response.status_code == 400
        assert "message" in response.json()

    def test_get_joke(self, client):
        response_chuck = client.get("/api/get-joke/chuck")
        response_dad = client.get("/api/get-joke/dad")
        assert response_chuck.status_code == 200
        assert response_dad.status_code == 200
        assert "joke" in response_chuck.json()
        assert "joke" in response_dad.json()


class TestJokeAPIView:

    def test_get_all_jokes(self, client, mocker, jokes_queryset):
        mocker.patch.object(
            joke.JokeAPIView,
            "get_queryset",
            return_value=jokes_queryset,
        )
        response = client.get("/api/joke")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_joke_by_id(self, client, mocker, chuck_joke):
        mocker.patch.object(
            joke.JokeAPIView,
            "get_object",
            return_value=chuck_joke,
        )
        response = client.get("/api/joke/1")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_create_joke(self, client, mocker, chuck_joke):
        payload = {"text": "a king cobra once bit Chuck Norris... after 5 days of terrible pain... the snake died"}
        mocker.patch.object(
            models.Joke.objects,
            "create",
            return_value=chuck_joke,
        )
        response = client.post("/api/joke", data=payload, format='json')
        assert response.status_code == 201
        assert "text" in response.json()

    def test_update_joke(self, client, mocker, chuck_joke, chuck_joke_updated):
        payload = {"text": "Updated Joke"}
        mocker.patch.object(
            models.Joke.objects,
            "update",
            return_value=chuck_joke,
        )
        mocker.patch.object(
            serializers.JokeSerializer,
            "update",
            return_value=chuck_joke_updated,
        )
        mocker.patch.object(
            joke.JokeAPIView,
            "get_object",
            return_value=chuck_joke,
        )
        response = client.put("/api/joke/1", data=payload, content_type='application/json')
        assert response.status_code == 200
        assert response.json() == payload

    def test_delete_joke(self, client, mocker, chuck_joke):
        mocker.patch.object(
            models.Joke,
            "delete",
            return_value=chuck_joke,
        )
        mocker.patch.object(
            joke.JokeAPIView,
            "get_object",
            return_value=chuck_joke,
        )
        response = client.delete("/api/joke/1", content_type='application/json')
        assert response.status_code == 204


class TestMCMAPIView:

    def test_mcm(self, client):
        payload = "30,13,28,29"
        mcm = 158340
        response = client.get("/api/mcm?numbers={}".format(payload))
        assert response.status_code == 200
        assert "mcm" in response.json()
        assert response.json()["mcm"] == mcm

    def test_incorrect_format_numbers(self, client):
        payload = "30,13,28,ij"
        response = client.get("/api/mcm?numbers={}".format(payload))
        assert response.status_code == 400


class TestPlusOneView:

    def test_plus_one(self, client):
        payload = "45"
        added_number = 46
        response = client.get("/api/plusone?number={}".format(payload))
        assert response.status_code == 200
        assert response.json()["added_number"] == added_number

    def test_incorrect_format_number(self, client):
        payload = "3j"
        response = client.get("/api/plusone?number={}".format(payload))
        assert response.status_code == 400
