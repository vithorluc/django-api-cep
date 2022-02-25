from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cep
from .serializers import CepSerializer
from rest_framework import status
from rest_framework.views import APIView 
from pycep_correios import get_address_from_cep, WebService, exceptions

class CepAPI(APIView):
    
    def get(self, request, pk=None, format=None):
        id = pk
        try:
            if id is not None:
                cep_data = Cep.objects.get(cep=pk)
                serializer = CepSerializer(cep_data)
                return Response(serializer.data)
            cep_data = Cep.objects.all()
            serializer = CepSerializer(cep_data, many=True)
            return Response(serializer.data)
        except Cep.DoesNotExist:
            return Response({'msg': 'Error get cep'}, status=status.HTTP_400_BAD_REQUEST) 

    def post(self, request, format=None):
        try:
            address = get_address_from_cep(request.data['cep'], webservice=WebService.APICEP)
            serializer = CepSerializer(data=address)
            if serializer.is_valid():
                cep = serializer.save()
                return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.CEPNotFound: 
            return Response({'msg': 'CEP not Found'}, status=status.HTTP_404_NOT_FOUND)
