from django.shortcuts import render

from library.models import Author


def index(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'index.html', context=context)
