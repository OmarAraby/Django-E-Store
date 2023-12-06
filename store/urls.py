from django.urls import path 
from . import views




app_name='store'



urlpatterns = [
    path('',views.product_list,name='home'),
    path('<slug:slug>',views.product_detail,name='product_detail' ),

    
]