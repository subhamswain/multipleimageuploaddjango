from django.shortcuts import render

from .models import Multiple
def upload(request):
    if request.method=='POST':
        images=request.FILES.getlist('images')
        for img in images:
            Multiple.objects.create(images=img)
    images=Multiple.objects.all()
    return render(request,"index.html",{'images':images})