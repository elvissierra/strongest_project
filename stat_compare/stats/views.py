from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Mon
from .serializers import ObjSerializer
from rest_framework.response import Response


# Create your views here.
class ObjGetView(APIView):
    
    def get(self, request, format=None):
        mons = Mon.objects.all()
        serializer = ObjSerializer(mons, many=True)
        return Response(serializer.data)
    
class ObjGetPutDelete(APIView):

    def get(request, mon_id):
        mon = get_object_or_404(Mon, id=mon_id)
        return Response(ObjSerializer(mon, context={"request" : request}).data)

