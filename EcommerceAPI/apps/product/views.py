from .models import Brand, Category, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Category is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def category_update(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Category is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Category is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response({'message': 'Category has been deleted.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def brand_list(request):
    brand = Brand.objects.all()
    serializer = BrandSerializer(brand, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def brand_detail(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Brand is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BrandSerializer(brand, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def brand_update(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Brand is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = BrandSerializer(instance=brand, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def brand_create(request):
    serializer = BrandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def brand_delete(request, pk):
    try:
        brand = Brand.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Brand is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    brand.delete()
    return Response({'message': 'Brand has been deleted.'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def product_list(request):
    product = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(data=product, many=True)
    serializer.is_valid()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Product is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(data=product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Product is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def product_delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'message': 'Product is not exists.'}, status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response({'message': 'Product has been deleted.'}, status=status.HTTP_204_NO_CONTENT)
