from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from app.models import Customer
from .serializers import CustomerSerializer
# Create your views here.

@csrf_exempt
@api_view (['GET', 'POST'])
def lista_clientes(request):
    if request.method=='GET':
        cliente = Customer.objects.all()
        serializer = CustomerSerializer(cliente, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)