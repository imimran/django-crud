
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.user_form,  name='user_form'),
    path('<int:id>/', views.user_form, name='user_update'),
    path('list/', views.user_list,  name='user_list'),
]