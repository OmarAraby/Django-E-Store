from django.shortcuts import render , get_object_or_404 , redirect
from django.urls import reverse
from .cart import Cart
from product.models import Product
from django.http import JsonResponse
# Create your views here.



def cart_summery(request):
	# Get The Cart
	cart = Cart(request)
	cart_products = cart.get_prods()
	quantity = cart.get_quants()
	all_total_price = cart.get_all_total_prices()
	single_total_price = cart.get_single_total_price()
	#cart_update = cart.update()

	


	# print(quantity)
	# print(single_total_price)


	context = {'cart_products':cart_products,
	'quantity':quantity,
	'single_total_price':single_total_price,
	'all_total_price':all_total_price,
	# 'cart_update':cart_update
	
	}
	return render(request, 'cart_summery.html' , context)







def cart_add(request):
	# get the cart
	cart = Cart(request)
	#test for Post
	if request.POST.get('action') == 'post' :
		# Get Stuff
		product_slug = request.POST.get('product_slug')
		product_qty = int(request.POST.get('product_qty')) 

		# Lookup Product in DB
		product = get_object_or_404(Product, PRDSlug=product_slug)

		# save to session 
		cart.add(product=product,quantity=product_qty)

		print('Product Name :',product.PRDName)

		# Get Cart Quantity
		cart_quantity = cart.__len__()
		# Return Response
		#response = JsonResponse({'Product Name':product.PRDName , 'Price':product.PRDPrice})
		
		response = JsonResponse({'qty':cart_quantity})
		return response








def cart_delete(request, product_slug):
    cart = Cart(request)
    cart.remove(product_slug)
    return redirect(reverse('cart:cart_summery'))








def cart_update(request):
	
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_slug = request.POST.get('product_slug')
		product_qty = int(request.POST.get('product_qty'))

		#product = get_object_or_404(Product, PRDSlug=product_slug)

		cart.update(product=product_slug, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		return response