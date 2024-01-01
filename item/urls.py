from django.urls import path

from . import views

app_name="item"

urlpatterns = [
    path("new",views.new,name="new"),
    path("detail/<int:pk>/",views.detail,name="detail"),
    path("edit/<int:pk>/",views.edit_item,name="edit"),
    path('delete/<int:pk>/',views.delete,name="delete"),
    path('browse_items/',views.browse_item,name="browse_items")
]