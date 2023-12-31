from .cart import Cart


# create context processor so our cart work and appears on all pages 


def cart(request):
	# Return the default data from our Cart

	return {'cart': Cart(request)}