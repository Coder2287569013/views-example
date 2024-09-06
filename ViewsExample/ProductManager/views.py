from django.shortcuts import render
from .models import Product, Review

# Create your views here.
def product_list(request):
    context = {
        "product_list": Product.objects.all()
    }

    return render(request, "ProductManager/product-list.html", context)

def product_overview(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        rating = request.POST.get("rating")

        Review.objects.create(
            product_id=pk,
            author=author,
            text=text,
            rating=rating
        )
    
    context = {
        "product_info": product,
        "reviews": product.reviews.all()
    }

    return render(request, "ProductManager/product-overview.html", context)