from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializer import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#
# class ProductAPIList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductAPIUpdate(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



#
# class ProductAPIView(APIView):
#     def get(self, request):
#         lst = Product.objects.all()
#         return Response({'title': ProductSerializer(lst, many=True).data})
#
#     def post(self, requset):
#         return Response({'title': 'Odejda'})

# class ProductAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
