from django.shortcuts import render
from django.http import HttpResponse
from .forms import Video_form
from .models import video

# Create your views here.
def hello(request):
    all_video = video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Uploaded")
    else:
        form=Video_form()
    return render(request, 'index.html',{"form":form, "all":all_video})

def index(request):
    return render(request, 'index.html')