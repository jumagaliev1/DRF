from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category
from .serializer import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Product.objects.all()[:3]
        return Product.objects.filter(pk=pk)
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.title})
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
