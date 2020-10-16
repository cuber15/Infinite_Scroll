from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('lorem/<int:word>',views.random,name="lorem"),
    path('loremtext',views.loremtext,name="loremtext")
]
