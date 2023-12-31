from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product , Category
from .filters import ProductFilter,CategoryFilter
from django.shortcuts import render, get_object_or_404
# Create your views here.




def product_list(request):
    product_list = Product.objects.all()
    ### filters Products
    myfilter = ProductFilter(request.GET, queryset=product_list)
    product_list = myfilter.qs

   




    paginator = Paginator(product_list, 8)  # Show X Products per page.

    page_number = request.GET.get("page")
    product_list = paginator.get_page(page_number)

    #category = Category.objects.all()


    context = {'products':product_list , 'myfilter':myfilter}
    return render(request, 'Product/product_list.html', context)





def product_detail(request,slug):
    product_detail = Product.objects.get(PRDSlug=slug)
    related_products = Product.objects.filter(
        PRDCategory=product_detail.PRDCategory,
        PRDBrand=product_detail.PRDBrand
    ).exclude(id=product_detail.id).order_by('-PRDCreated')[:4]
    
    
    context = {'product_detail':product_detail, 'related_products':related_products}
    

    return render(request,'Product/product_detail.html',context)






# def category_list(request):
#     category = Category.objects.all()
#     return render(request, 'category_list.html', {'categories': category})







def category_detail(request, slug):
    category = get_object_or_404(Category, CATSlug=slug)
    products = Product.objects.filter(PRDCategory=category)
    myfilter = CategoryFilter(request.GET, queryset=products)
    products = myfilter.qs

    context = {'category': category, 'products': products,'myfilter':myfilter}
    return render(request, 'Category/category_detail.html', context)









    