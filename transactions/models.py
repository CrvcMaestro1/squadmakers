from django.db import models


class JokeType(models.TextChoices):
    chuck = "chuck", "CHUCK"
    dad = "dad", "DAD"
    random = "random", "RANDOM"


class Joke(models.Model):
    text = models.TextField(verbose_name="Text", max_length=256)
