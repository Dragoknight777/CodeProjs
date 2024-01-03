from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from NewApp.models import Game, Developer
from NewApp.serializers import GameSerializer, DeveloperSerializer

# Create your views here.

@csrf_exempt
def developerApi(request, id=0):
    if request.method=='GET':
        developer = Developer.objects.all()
        developer_serializer = DeveloperSerializer(developer, many=True)
        return JsonResponse(developer_serializer.data, safe=False)
    elif request.method=='POST':
        developer_data=JSONParser().parse(request)
        developer_serializer = DeveloperSerializer(data=developer_data)
        if developer_serializer.is_valid():
            developer_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        developer_data = JSONParser().parse(request)
        developer = Developer.objects.get(DeveloperId = developer_data['DeveloperId'])
        developer_serializer = DeveloperSerializer(developer, data = developer_data)
        if developer_serializer.is_valid():
            developer_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        developer=Developer.objects.get(DeveloperId = id)
        developer.delete()
        return JsonResponse("Deleted Successfully", safe = False)