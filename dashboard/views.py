from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from item.models import Item

# Create your views here.

@login_required
def dashboard(request):
    item = Item.objects.filter(created_by=request.user)
    context = {"items": item}
    return render(request,'dashboard/index.html',context)
