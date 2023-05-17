from rest_framework.decorators import api_view
from rest_framework.response import Response
import librosa
import datetime
import os
from emosic_essentials import AudioAnalysis
from keras.models import load_model
from django.conf import settings
import numpy as np
import pickle


TRAINED_MODEL = load_model(os.path.join(settings.BASE_DIR, 'model-0.8723.h5'))
print(TRAINED_MODEL.summary())
with open(os.path.join(settings.BASE_DIR, 'feature_transcoder.pckl'), 'rb') as f:
    a = pickle.load(f)


@api_view(['POST'])
def home(request):
    time = str(datetime.datetime.now())
    wav_file = time + '.wav'
    f = request.FILES['audio']
    with open(wav_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    y, sr = librosa.load(wav_file, sr=22050)
    os.remove(wav_file)
    return Response({'emotion': a.decode(TRAINED_MODEL.predict(np.expand_dims(np.array(AudioAnalysis().get_features(y, sr)), 1).reshape(1, -1))[0].tolist())})
