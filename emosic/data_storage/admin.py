from django.contrib import admin
from .models import Emotion, AudioData, Music

admin.site.register(Emotion)
admin.site.register(AudioData)
admin.site.register(Music)
