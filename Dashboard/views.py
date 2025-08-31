from django.shortcuts import render, redirect, HttpResponse , get_object_or_404
from shop.models import Category, Item
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required 
from django.core.exceptions import PermissionDenied
# import matplotlib.pyplot as plt      #later for data visualization mnamn stuff with htmx

def superuser_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view  #I need to understand this custom decorator if I'm gonna be a django develoer sometime soon and work on my own decorators because decorators are so cool.


# Create your views here.
# def dashboard(request):
#     items = Item.objects.count()
#     categories = Category.objects.count()
#     return render(request, 'Dashboard/index.html',{'items':items, 'categories':categories})
@superuser_required
def dashboard(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_category_id = request.POST.get('item_category')  # This is a string ID
        price = request.POST.get('price')
        description = request.POST.get('description')

        try:
            category_obj = Category.objects.get(pk=item_category_id)
        except Category.DoesNotExist:
            return HttpResponse("Invalid category selected.", status=400)

        Item.objects.create(
            item_name=item_name,
            item_category=category_obj,
            price=price,
            description=description
        )
        return redirect('item:shop')
    form = CategoryForm()
    categories = Category.objects.all()
    items = Item.objects.all()
    return render(request, 'Dashboard/index.html', {'categories': categories, 'items': items,'form':form})


@superuser_required
def category_creation(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard')
    else:
        form = CategoryForm()
    categories = Category.objects.all()
    items = Item.objects.all()
    context = {
    'form':form,
    'categories': categories, 
    'items': items
    }
    return render(request, 'Dashboard/index.html',context)


# @superuser_required
# def search_log(request,pk):
#     query = request.GET.get('search','')
#     obj = get_object_or_404(Category, pk=pk)
#     logs = LogEntry.objects.get_for_object(obj)
#     history = query
