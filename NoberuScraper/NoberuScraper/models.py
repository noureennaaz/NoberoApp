

# def insert_product(data):
    
#     # api_url = 'http://127.0.0.1:8000/api/products/'  
#     headers = {'Content-Type': 'application/json'}
#     from NoberoApp.models import Product, ProductSKU
#     product = Product(
#         category=data['category'],
#         url=data['url'],
#         title=data['title'],
#         price=data['price'],
#         MRP=data['MRP'],
#         last_7_day_sale=data['last_7_day_sale'],
#         fit=data['fit'],
#         fabric=data['fabric'],
#         neck=data['neck'],
#         sleeve=data['sleeve'],
#         pattern=data['pattern'],
#         length=data['length'],
#         description=data['description'],
#     )
#     product.save()

#     # Save available_skus if it's a related model
#     for sku in data['available_skus']:
#         ProductSKU.objects.create(
#             product=product,
#             color=sku['color'],
#             sizes=sku['size']
#         )