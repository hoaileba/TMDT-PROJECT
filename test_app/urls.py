from django.urls import path

from . import views

urlpatterns = [
    path('hoaileba', views.index, name='index'),
    path('additem', views.add_item_view, name = "additem"),
    path('register', views.register_view, name = "register"),
    path('login', views.login_view, name = "login"),
]
