from django.urls import path 
from .views import dashboard, category_creation
app_name = 'dashboard'
urlpatterns =[
    # path('dashboard/', dashboard,name='dashboard'),
    path('dashboard/',dashboard , name= 'dashboard'),
    path('category_creation/', category_creation, name='category_creation'),
]