"""point_of_sale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from datarepo.views import add_category, update_category, details_of_category, list_of_category, delete_category, add_product, update_product, delete_product, product_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_category/', add_category, name='add_category'),
    path('update_category/', update_category, name='update_category'),
    path('details_of_category/', details_of_category, name='details_of_category'),
    path('list_of_category/', list_of_category, name='list_of_category'),
    path('delete_category/', delete_category, name='delete_category'),
    path('add_product/', add_product, name='add_product'),
    path('update_category/', update_category, name='update_category'),
    path('delete_product/', delete_product, name='delete_product'),
    path('product_list/', product_list, name='product_list'),

]
