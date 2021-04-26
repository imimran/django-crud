from django.shortcuts import render
from .form import UserForm

# Create your views here.

def user_list(request):
    return render(request, 'users/list.html')

def user_form(request):
    form = UserForm()
    return render(request, 'users/form.html', {'form': form})

def user_delete(request):
     return 