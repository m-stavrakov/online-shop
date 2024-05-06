from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Item
# pk is the primary key
# this will show details for each item
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/index.html', {
        'item': item
    })