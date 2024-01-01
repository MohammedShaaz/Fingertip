from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewItemForm,EditItemForm
from .models import Category,Item
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def new(request):
    if request.method =="POST":
        form = NewItemForm(request.POST,request.FILES)

        item = form.save(commit=False)
        item.created_by = request.user
        item.save()

        return redirect("core:index")

    else:
        form = NewItemForm()
    context = {"form" : form}
    return render(request,'item/new_item.html',context)

def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_item = Item.objects.filter(category = item.category,is_sold=False).exclude(pk=pk)

    context = {'item':item,'related_item':related_item}
    return render(request,'item/detail.html',context)


@login_required
def edit_item(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()

        return redirect("item:detail",pk=item.id)
    else:
        form = EditItemForm(instance=item)
    context = {"form":form}
    return render(request,'item/edit_item.html',context)

@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by = request.user)
    item.delete()

    return redirect("core:index")


def browse_item(request):
    query = request.GET.get('query','')
    category_id_rec = request.GET.get('category',0)


    categories = Category.objects.all()
    items = Item.objects.filter(is_sold = False)

    if category_id_rec :
        items = items.filter(category_id=category_id_rec)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {"items":items, "categories": categories, "query" :query, "category_id" :int(category_id_rec)}


    return render(request,'item/browse_item.html',context)
