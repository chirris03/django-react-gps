# expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add-expense/', views.add_expense, name='add_expense'),
    path('add-consumption/', views.add_consumption, name='add_consumption'),
    path('add-discarded-item/', views.add_discarded_item, name='add_discarded_item'),
]
