from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import student
from .serializer import studentSerializer


@api_view(['GET'])
def home(request):
    obj = student.objects.all()
    serailizer_data= studentSerializer(obj, many = True)
    return Response(serailizer_data.data)

@api_view(['POST'])
def add_data(request):
    obj = studentSerializer(data = request.data)
    if obj.is_valid():
        obj.save()
        return redirect('home')
    else:
        return Response({"message": "data is not inserted!!!"})


@api_view(['PATCH', "DELETE"])
def update_data(request, pk):
    if request.method == "PATCH":
        data = student.objects.get(id = pk)
        user_data = request.data
        obj = studentSerializer(data,user_data)
        if obj.is_valid():
            obj.save()
            return redirect('home')
        return Response({"message": "Data Deleted Successfully"})
    if request.method == "DELETE":
        data = student.objects.get(id = pk)
        data.delete()
        return Response({"message": "Data deleted successfully"})
    
@api_view(['GET'])
def specific_data(request, pk):
    obj = student.objects.get(id = pk)
    serialize_data = studentSerializer(obj)
    return Response(serialize_data.data)
