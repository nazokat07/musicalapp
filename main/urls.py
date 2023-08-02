from django.urls import path
from .views import (
    home,
    contact,
    sale,
    create,
    sale_detail,
    about,
    sale_delete,
    sale_update
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('sale/', sale, name='sale'),
    path('sale/<pk>/', sale_detail, name='sale_detail'),
    path('sale/<pk>/delete', sale_delete, name='sale_delete'),
    path('sale/<pk>/update', sale_update, name='sale_update'),
    path('create/', create, name='create'),
    path('contact/', contact, name='contact'),
]