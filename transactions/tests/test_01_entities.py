import pytest

from transactions import models

"""
START FIXTURES
"""


@pytest.fixture
def chuck_joke():
    return models.Joke(
        text="a king cobra once bit Chuck Norris... after 5 days of terrible pain... the snake died"
    )


@pytest.fixture
def dad_joke():
    return models.Joke(
        text="My dog used to chase people on a bike a lot. It got so bad I had to take his bike away."
    )


@pytest.fixture
def empty_joke():
    return models.Joke(
        text=None
    )


"""
END FIXTURES
"""


class TestJoke:
    def test_joke(self, chuck_joke, dad_joke):
        assert chuck_joke.text is not ""
        assert chuck_joke.text is not None
        assert dad_joke.text is not None
        assert dad_joke.text is not None

    def test_empty_joke(self, empty_joke):
        assert empty_joke.text is None
