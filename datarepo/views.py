from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

from .models import Product, Category


def add_category(request):
    category_name = request.GET['category_name']
    product_name = request.GET['product_name']
    price = request.GET['price']
    quantity = request.GET['quantity']
    created = request.GET['created']
    new_category = Category.objects.create(
        category_name=category_name,
        product_name=product_name,
        price=price,
        quantity=quantity,
        created=created,
    )
    new_category.save()
    return jsonResponse("<h1> new category is added<h1>")


def update_category(request):
    category_id = request.GET['category_id']
    category_name = request.GET['category_name']
    product_name = request.GET['product_name']
    price = request.GET['price']
    quantity = request.GET['quantity']
    created = request.GET['created']

    updated = Category.objects.get(id=int(category_id))

    updated.category_name = category_name
    updated.product_name = product_name
    updated.price = price
    updated.quantity = quantity
    updated.created = created
    updated.save()

    content = {
        'category_id': updated.id,
        'category_name': updated.category_name,
        'product_name': updated.product_name,
        'price': updated.price,
        'quantity': updated.quantity,
        'created': updated.created
    }
    return JsonResponse(content, safe=False)


def details_of_category(request):
    category_of_product = request.GET['category_of_product']
    product_details = Category.objects.get(int=int(category_of_product))
    list_of_product = Product.objects.filter(product_category=product_details)
    list_of_category_products = []
    for product in list_of_product:
        temp_category = {
            'category_of_product': str(product.category_of_product),
            'price': product_price,
            'created': product.created,
        }
        list_of_category_products.append(temp_category)
    return JsonResponse(list_of_category_products, safe=False)


def list_of_category(request):
    categorys = Category.objects.all()
    response_categorys = []
    for category in categorys:
        temp_category = {
            'category_id': category.id,
            'category_name': category.category_name,
            'product_name': category.product_name,
            'price': category.price,
            'quantity': category.quantity,
            'created': category.created
        }
        response_categorys.append(temp_category)
    content = {
        "categorys": response_categorys
    }
    return JsonResponse(content, safe=False)


def delete_category(request):
    category_id = request.GET['category_id']
    category = Category.objects.get(id=int(category_id))
    category.delete()
    content = {
        "message": "category has been deleted"
    }
    return JsonResponse(content, safe=False)



def add_product(request):
    product_name = request.GET['product_name']
    product_price = request.GET['product_price']
    product_quantity = request.GET['product_quantity']
    product_category = request.GET['product_category']
    date_time = request.GET['date_time']
    new_product = Product.objects.create(

        product_name=product_name,
        product_price=product_price,
        product_quantity=product_quantity,
        product_category=product_category,
        date_time=date_time,
    )
    new_product.save()
    return HttpResponse("<h1> new product has been added <h1>")


def update_product(request):
    product_id = request.GET['product_id']
    product_name = request.GET['product_name']
    product_price = request.GET['product_price']
    product_quantity = request.GET['product_quantity']
    product_category = request.GET['product_category']
    date_time = request.GET['date_time']

    updated = Product.objects.get(id=int(product_id))

    updated.product_name = product_name
    updated.product_price = product_price
    updated.product_quantity = product_quantity
    updated.product_category = product_category
    updated.date_time = date_time

    updated.save()

    content = {
        'product_id': updated.id,
        'product_name': updated.product_name,
        'product_price': updated.product_price,
        'product_quantity': updated.product_quantity,
        'product_category': updated.product_category,
        'date_time': updated.date_time
    }

    return JsonResponse(content, safe=False)


def delete_product(request):
    product_id = request.GET['product_id']
    product = Product.objects.get(id=int(product_id))
    product.delete()
    content = {
        "message": "product has been deleted"
    }
    return JsonResponse(content, safe=False)


def product_list(request):
    products = Product.objects.all()
    response_products = []
    for product in products:
        temp_product = {
            'product_id': product.id,
            'product_name': product.product_name,
            'product_price': product.product_price,
            'product_quantity': product.product_quantity,
            'date_time': product.date_time
        }
        response_products.append(temp_product)
    content = {
        "products": response_products
    }
    return JsonResponse(content, safe=False)
