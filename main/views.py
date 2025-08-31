from django.shortcuts import render, redirect 
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from shop.models import Category , Item
# from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    category = Category.objects.all()[0:10]
    item = Item.objects.filter(is_sold =False)
    context = {
        'category':category ,
        'item':item,
    }
    return render(request, 'main/index.html',context)

def filter_items(request):
    # Get the list of category IDs from the checked boxes
    # request.GET.getlist('category_ids') will get all values with the name 'category_ids'
    selected_category_ids = request.GET.getlist('category_ids')
    # print(selected_category_ids)  # For debugging purposes

    # Start with a base queryset of all items you want to consider
    items = Item.objects.filter(is_sold=False)

    # If categories were selected, chain filters to create the "AND" logic
    if selected_category_ids:
        for cat_id in selected_category_ids:
            items = items.filter(item_category__CategoryId=cat_id)
    
    # Note: We are now rendering the PARTIAL, not the whole index page.
    # This is the key to htmx's efficiency.
    context = {
        'item': items,
    }
    return render(request, 'main/partials/filter.html', context)


# I've removed your flter_partial view as it's replaced by filter_items.
# ... your other views (signup, login, etc.) remain the same ...

def aboutus(request):
    return render(request, 'main/aboutus.html')

def signup(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('main:login')
    else:
        form = SignUpForm()
    context = {
        'form':form
    }
    return render(request, 'main/signup.html',context)

def login(request):
    return render(request, 'main/login.html')
@login_required
def logout(request):
    logout(request)
    return redirect('main:index')
@login_required
def profile(request):
    return render(request, 'main/profile.html')
def success(request):
    return render(request, 'main/success.html')