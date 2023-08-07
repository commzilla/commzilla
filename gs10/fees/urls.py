from django.urls import path
from . import views

urlpatterns = [
    path('cb/',views.bangla),
    path('ce/', views.english),
]