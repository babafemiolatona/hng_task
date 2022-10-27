from .models import Info
from .serializers import InfoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def info_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        info = Info.objects.all()
        serializer = InfoSerializer(info, many=True)
        return Response(serializer.data)