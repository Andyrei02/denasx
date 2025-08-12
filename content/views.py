from django.shortcuts import render
# from .models import SocialLink, ImageAsset, Description


# def index(request):
#     return render(request, 'content/index.html', {
#         'links': SocialLink.objects.all(),
#         'images': ImageAsset.objects.all(),
#         'description': Description.objects.first()
#     })

from .models import HeaderContent

def index(request):
    content = HeaderContent.objects.first()
    return render(request, "index.html", {"content": content})
