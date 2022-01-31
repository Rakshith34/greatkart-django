from django.shortcuts import render
from store.models import Product,ReviewRating
from category.models import Category


def home(request):
    products = Product.objects.all()

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {'products':products,
               'reviews':reviews,
               }
    return render(request,'home.html',context)
