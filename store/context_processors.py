from .models import Category

def category_filter(request):
    categories = Category.objects.all()
    return {'categories': categories}