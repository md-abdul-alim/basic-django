from django.urls import path

from .views import (
                product_detail_view,
                product_create_view,
                RawProduct_create_view,
                robust_product_create_view,
                dynamic_Url_routing_view,
                product_delete_view
            )
app_name='products'
urlpatterns = [
    path('details/', product_detail_view,name='product_detail_view'),
    path('create/', product_create_view,name='product_create_view'),
    path('raw_create/', RawProduct_create_view,name='RawProduct_create_view'),
    path('robust_create/', robust_product_create_view,name='robust_product_create_view'),
    path('dynamic_view/<int:id>/', dynamic_Url_routing_view,name='dynamic_Url_routing_view'),
    path('delete/<int:id>/', product_delete_view,name='product_delete_view'),
]


'''
urlpatterns = [
    path('product_detail_view/', product_detail_view,name='product_detail_view'),
    path('create/', product_create_view,name='product_create_view'),
    path('raw_create/', RawProduct_create_view,name='RawProduct_create_view'),
    path('robust_create/', robust_product_create_view,name='robust_product_create_view'),
    path('dynamic_product_view/<int:id>/', dynamic_Url_routing_view,name='dynamic_Url_routing_view'),
    path('product_delete_view/<int:id>/', product_delete_view,name='product_delete_view'),
]
'''