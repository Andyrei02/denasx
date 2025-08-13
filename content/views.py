from django.shortcuts import render
from .models import HeaderContent


def index(request):
    content = HeaderContent.objects.first()
    return render(request, "index.html", {"content": content})
