from django.shortcuts import render

# Create your views here.

def user_list(request):
    return render(request, 'users/list.html')

def user_form(request):
     return render(request, 'users/form.html')

def user_delete(request):
     return 