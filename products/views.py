from products.models import Product
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    query = request.GET.get("query")
    if query is not None:
        products = products.filter(title__icontains=query)
    string = "<br>".join([str(p) for p in products])
    return HttpResponse(string)
