from django.shortcuts import render, redirect
from .form import UserForm

# Create your views here.


def user_list(request):
    return render(request, 'users/list.html')


def user_form(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'users/form.html', {'form': form})

    else:
        form = UserForm(request.POST)
        if form.is_valid() :
            form.save()
        return redirect('/user/list.html')


def user_delete(request):
    return
