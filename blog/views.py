from django.shortcuts import render
from .models import Post,CV
from .forms import CVform
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def editor(request):
    cvs = CVform()
    form = CVform(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
    return render(request, 'blog/editor.html',{'form':form})

def cv(request):
    cv_edus = CV.objects.all()
    return render (request, 'blog/cv.html',{'cv_edus':cv_edus})