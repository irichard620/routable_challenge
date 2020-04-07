from django.http import HttpResponse

from transactions.models import Item


def create_item(request):
    item = Item.create(amount_cents=request.POST['amount_cents'])
    item.save()
    return HttpResponse("Item successfully created")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
