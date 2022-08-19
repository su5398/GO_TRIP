from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
# Create your views here.


def blog(request):
    posts = Post.objects.filter().order_by('-counting')
    return render(request, 'blog.html', {'posts':posts})

def blog2(request):
    posts = Post.objects.filter().order_by('-counting')
    return render(request, 'serviceapp/main.html', {'posts':posts})


def write(request):
    if request.method == "POST" or request.method == 'FILES':  #입력값 저장
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/blog')
    else:
        form = PostForm()
    return render(request, 'write.html', {'form':form})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Post, pk=blog_id)
    blog_detail.counting += 1
    blog_detail.save()
    return render(request, 'detail.html', {'blog_detail':blog_detail})


def search(request):
    blogs = Post.objects.all().order_by('-counting')

    q = request.POST.get('q', "")

    if q:
        blogs = blogs.filter(제목__icontains=q)
        return render(request, 'search.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'search.html')
