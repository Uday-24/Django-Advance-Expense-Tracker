from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fetch_expense/', views.fetch_expense, name="fetch_expense"),
    path('update_expense/', views.update_expense, name="update_expense"),
    path('delete_expense/', views.delete_expense, name="delete_expense"),
]