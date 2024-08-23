# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.conf import settings
# from .serializers import MyModelSerializer

# @api_view(['POST'])
# def create_my_model(request):
#     serializer = MyModelSerializer(data=request.data)
#     if serializer.is_valid():
#         # Access the MongoDB collection
#         collection = settings.MONGO_DB['mycollection']

#         # Insert data into MongoDB
#         collection.insert_one(serializer.data)

#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# views.py
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['POST'])
def product_list(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



def test_product_view(request):
    try:
        # Fetch all products (if any) from the database
        products = Product.objects.all()
        return HttpResponse(f"Found {products.count()} products.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
    
    from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
import subprocess
from django.http import JsonResponse

@api_view(['POST'])
def insert_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def trigger_scrapy_spider(request):
    try:
        # Adjust the command as needed to match your scrapy setup
        command = 'scrapy crawl men'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            return JsonResponse({'status': 'Spider started successfully', 'output': result.stdout}, status=200)
        else:
            return JsonResponse({'status': 'Failed to start spider', 'error': result.stderr}, status=500)
    
    except Exception as e:
        return JsonResponse({'status': 'Error', 'error': str(e)}, status=500)