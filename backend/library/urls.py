from django.urls import path, include

from library.views import index

urlpatterns = [
    path('', index, name='index'),
]
