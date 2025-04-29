from django.shortcuts import render
from blog.models import  Post, Categoria

# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts, 
                                              'categorias':categorias})
    

def filter_categoria(request, categoria_id):
    categoria = Post.objects.filter(categorias=categoria_id)
    items = Categoria.objects.all()
    return render(request, 'blog/categorias.html', {'categorias':categoria,
                                                    'items':items,})