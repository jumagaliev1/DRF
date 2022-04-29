from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Product

# class ProductModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        # fields = ('title', 'city', 'category', 'description')
        fields = ('__all__')

#
# def encode():
#     model = ProductModel('Odejda', 'Content: Ne Odejda')
#     model_sr = ProductSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)