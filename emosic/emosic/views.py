from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def home(request):
    print(request.FILES['audio'])
    return Response({})
