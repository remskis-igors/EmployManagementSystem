from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('some-path/', views.employee_list, name='some-view-name'),
]
