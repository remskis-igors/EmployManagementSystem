from django.shortcuts import render
from .models import MyModel

def home(request):
    data = MyModel.objects.all()
    return render(request, 'myapp/home.html', {'data': data})
