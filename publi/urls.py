from django.urls import path
from .views import home,post,fotos,detallePost

urlpatterns = [
    path('',home, name='index'),
    path('post/',post, name='post'),
    path('fotos/',fotos,name="fotos"),
    path('<slug:slug>', detallePost, name = 'detalle_post'),
]