from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .models import Repair
from django.http import Http404 



from .forms import ProductForm

def home(request):
    return render(request,'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def sale(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(
        request,
        'main/sale.html',
        context
    )

def sale_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'error/404.html')
    #product = get_object_or_404(Product, id=pk)
    context = {
        'product':  product
    }
    return render(request, 'main/sale_detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            '''cd = form.cleaned_data
            Product.objects.create(
                title=cd['title'],
                image=cd['image'],
                description = cd['description'],
                price = cd['price'],
                author = cd['author'],
                condition = cd['condition']
            )'''
        return redirect(to='sale')
    else:
        form = ProductForm()

    #print(ProductForm(request.POST).is_valid())
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


def contact(request):
    return render(request, 'main/contact.html')

def sale_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect(to='sale')

def sale_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']
            condition = form.cleaned_data['condition']

            product.title = title
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.condition = condition
            product.save()
            return redirect(to='sale')

    context = {
        'form': form
    }
    return render(request, 'main/update.html', context)

