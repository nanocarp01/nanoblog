from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden

def csrf_error_handler(request, reason=""):
    return HttpResponseForbidden("Error CSRF al iniciar sesión: {}".format(reason))

def home(request):
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(post, 2)
    page = request.GET.get('page') 
    post = paginator.get_page(page)
    return render (request,'index.html',{'post':post})

def detallePost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,"post.html",{"detalle_post":post})

def post(request):
    post = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Lectura'))
    return render (request,'post.html',{'post':post})

def fotos(request):
    fotos = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Fotos'))
    return render (request,'fotos.html', {'fotos':fotos})
