from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Mon
from .serializers import ObjSerializer
from rest_framework.response import Response


class ObjGetView(APIView):
    """
    Get all objects
    """
    def get(self, request, format=None):
        mons = Mon.objects.all()
        serializer = ObjSerializer(mons, many=True)
        return Response(serializer.data)
    
class ObjGetPutDelete(APIView):
    """
    Get specific object
    """
    def get(request, mon_id):
        note = get_object_or_404(Mon, id=mon_id)
        return Response(ObjSerializer(note, context={"request": request}).data)

#compare based on stat here logic needed
        
