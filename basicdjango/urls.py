"""basicdjango URL Configuration

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
from django.urls import path, include
#from pages import views
from pages.views import home_view, template_tags_filters_view
# from products.views import (
#                             product_detail_view,
#                             product_create_view,
#                             RawProduct_create_view,
#                             robust_product_create_view,
#                             dynamic_Url_routing_view,
#                             product_delete_view
#                         )
urlpatterns = [
    #path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('template_tags_filters/', template_tags_filters_view,
         name='template_tags_filters'),
    # path('product_detail_view/', product_detail_view,name='product_detail_view'),
    # path('create/', product_create_view,name='product_create_view'),
    # path('raw_create/', RawProduct_create_view,name='RawProduct_create_view'),
    # path('robust_create/', robust_product_create_view,name='robust_product_create_view'),
    # path('dynamic_product_view/<int:id>/', dynamic_Url_routing_view,name='dynamic_Url_routing_view'),
    # path('product_delete_view/<int:id>/', product_delete_view,name='product_delete_view'),
    path('products/', include('products.urls')),
    path('articles/', include('class_based_work.urls')),
    path('courses/', include('courses.urls')),
    path('mycourses/', include('func_view_under_cls_view.urls'))
]
