from django.urls import path
from .views import *

urlpatterns = [
    path('books',BookListAPIView.as_view(),name='Book-List'),
    path('add/book',BookCreateAPIView.as_view(),name='Add-Book'),
    path('edit/book/<int:pk>',BookRetriveUpdateAPIView.as_view(),name='Edit-Book'),
    path('delete/book/<int:pk>',BookDestroyAPIView.as_view(),name='Delete-Book'),

    path('orders',OrderLsitAPIView.as_view(),name='Orders'),
    path('add/order',OrderCreateAPIView.as_view(),name='Add-order'),
    path('edit/order/<int:pk>',OrderRetriveUpdateAPIView.as_view(),name='Edit-order'),
    path('delete/order/<int:pk>',OrderDestroyAPIView.as_view(),name='Delete-order'),

]  
