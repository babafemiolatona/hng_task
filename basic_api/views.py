from .models import Info
from .serializers import InfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def info_list(request):
    info = Info.objects.get()
    serializer = InfoSerializer(info)
    return Response(serializer.data)
