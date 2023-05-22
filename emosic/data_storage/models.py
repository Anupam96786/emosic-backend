from django.db import models


class Emotion(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False, unique=True, primary_key=True)


class AudioData(models.Model):
    features = models.JSONField()
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)


class Music(models.Model):
    url = models.URLField(blank=False, null=False, unique=True, primary_key=True)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
