from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.




def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 8)  # Show X Products per page.

    page_number = request.GET.get("page")
    product_list = paginator.get_page(page_number)


    context = {'products':product_list}
    return render(request, 'Product/product_list.html', context)





def product_detail(request,slug):
    product_detail = Product.objects.get(PRDSlug=slug)
    related_products = Product.objects.filter(
        PRDCategory=product_detail.PRDCategory,
        PRDBrand=product_detail.PRDBrand
    ).exclude(id=product_detail.id).order_by('-PRDCreated')[:4]
    
    
    context = {'product_detail':product_detail, 'related_products':related_products}
    

    return render(request,'Product/product_detail.html',context)

