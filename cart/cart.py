from product.models import Product

class Cart():
	def __init__(self,request):
		self.session = request.session


		# Get the cuurent session Key if it exists

		cart = self.session.get('session_key')


		# if USer is New , No Session key , create one

		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}



		# Making Sure that cart is available on all pages of site

		self.cart = cart


	def add(self, product, quantity):
	    product_slug = product.PRDSlug
	    product_qty = str(quantity)

	    if product_slug in self.cart:
	        # If the product is already in the cart, you can implement your logic here
	        self.cart[product_slug] += product_qty
	    else:
	        self.cart[product_slug] = int(product_qty)

	    self.session.modified = True



	# Count anything in the cart

	def __len__(self):
		return len(self.cart)


	def get_prods(self):
    	# Get slugs from cart
	    product_slugs = self.cart.keys()

	    # Use slugs to lookup products in the database model
	    products = Product.objects.filter(PRDSlug__in=product_slugs)

	    return products



	def get_quants(self):
	    quantity = self.cart
	    return quantity 

	def get_all_total_prices(self):
	    total_price = 0

	    for product_slug, quantity_value in self.cart.items():
	        product = Product.objects.get(PRDSlug=product_slug)
	        total_price += product.PRDPrice * quantity_value

	    return total_price

	def get_single_total_price(self):
	    total_price = {}

	    for product_slug, quantity_value in self.cart.items():
	        product = Product.objects.get(PRDSlug=product_slug)
	        total_price[product_slug] = product.PRDPrice * quantity_value

	    return total_price




	def update(self, product, quantity):
		product_slug = str(product)
		product_qty = int(quantity)

		# Get cart
		ourcart = self.cart
		# Update Dictionary/cart
		ourcart[product_slug] = product_qty

		self.session.modified = True

		thing = self.cart
		return thing



	def remove(self, product_slug):
	    if product_slug in self.cart:
	        del self.cart[product_slug]
	        self.session.modified = True

