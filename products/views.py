from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
# step 2
from .forms import ProductForm, RawProductForm, robust_ProductForm
from django.http import Http404
# Create your views here.


def product_detail_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products/product_detail_view.html", context)


def product_create_view(request):
    # print(request.GET["title"])
    # print(request.POST["title"])
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        # Product.objects.create(title=my_new_title)
        print(my_new_title)

    context = {
    }
    return render(request, "products/product_create.html", context)


'''
#build
def product_create_view(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
    context={
        'form':form
    }
    return render(request,"products/product_create.html",context)
'''


def RawProduct_create_view(request):
    my_row_form = RawProductForm()
    if request.method == "POST":
        my_row_form = RawProductForm(request.POST)
        if my_row_form.is_valid():
            print(my_row_form.cleaned_data)
            Product.objects.create(**my_row_form.cleaned_data)
        else:
            print(my_row_form.errors)
    context = {
        'form': my_row_form
    }
    return render(request, "products/RawProduct_create.html", context)


def robust_product_create_view(request):
    '''
    initial_data={
        'description':"This is robust description."
    }
    #form=robust_ProductForm(request.POST or None) #if we don't use initial_data this line is correct
    obj=Product.objects.get(id=1) # for update data from database
    form=robust_ProductForm(request.POST or None,initial=initial_data,instance=obj)
    '''
    form = robust_ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = robust_ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/robust_ProductForm_create.html", context)


def dynamic_Url_routing_view(request, id):
    # products = Product.objects.get(id=id) #this is correct
    # this is also correct.but it will handle doesNotExist error
    products = get_object_or_404(Product, id=id)

    # or
    # try:
    #     products= Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        'product': products
    }
    return render(request, "products/dynamic_product_detail.html", context)

def product_delete_view(request, id):
    products = get_object_or_404(Product, id=id)
    if request.method == "POST":
        products.delete()
        #return redirect('../../')
        return redirect('products:product_detail_view')
    context = {
        'product': products
    }
    return render(request, "products/product_delete.html", context)