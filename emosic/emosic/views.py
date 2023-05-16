from rest_framework.decorators import api_view
from rest_framework.response import Response
import librosa
import datetime
import os
import emosic_essentials
from keras.models import load_model
from django.conf import settings
import numpy as np


TRAINED_MODEL = load_model(os.path.join(settings.BASE_DIR, 'model-0.8651.h5'))
print(TRAINED_MODEL.summary())


@api_view(['POST'])
def home(request):
    time = str(datetime.datetime.now())
    webm_file = time + '.webm'
    f = request.FILES['audio']
    with open(webm_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    y, sr = librosa.load(webm_file, sr=22050)
    print(TRAINED_MODEL.predict(np.expand_dims(np.array(emosic_essentials.AudioAnalysis().get_features(y, sr)), 1).reshape(1, -1)))
    os.remove(webm_file)
    return Response({})
