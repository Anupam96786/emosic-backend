from rest_framework.decorators import api_view
from rest_framework.response import Response
import librosa
import datetime
import os


@api_view(['POST'])
def home(request):
    time = str(datetime.datetime.now())
    webm_file = time + '.webm'
    f = request.FILES['audio']
    with open(webm_file, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    y, sr = librosa.load(webm_file, sr=22050)
    print(y)
    os.remove(webm_file)
    return Response({})
