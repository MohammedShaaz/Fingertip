from django.shortcuts import render,redirect
from item.models import Item,Category
from .forms import SignupForm
from django.contrib.auth import logout
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)
    category = Category.objects.all()

    context = {"items" : items,"categories":category}
    return render(request,'core/index.html',context)


def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect("core:index")
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request,'core/signup.html',context)

def logout_view(request):
    logout(request)
    return redirect("core:index")

