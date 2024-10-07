from django.urls import path 

from . import views

urlpatterns = [
    path('detail/', views.product_api_view, name='product_api_view')
]
