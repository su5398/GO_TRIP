from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from blogapp.models import Post


def intro(request):
    return render(request, 'serviceapp/intro.html')


def main(request):
    nac_rank = Post.objects.filter().order_by('-counting')
    nac_rank = nac_rank[:3]
    return render(request, 'serviceapp/main.html', {'nac_rank':nac_rank})


def course(request):
    return render(request, 'serviceapp/course.html')


def login(request):
    return render(request, 'serviceapp/login.html')


def membership(request):
    return render(request, 'serviceapp/membership.html')


def write(request):
    return render(request, 'serviceapp/write.html')

def create(request):
  if request.method=="POST":
    post = Post()
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    post.image = request.FILES['image']
    post.save()
    return redirect('/detail/'+str(post.id),{'post':post})
  else:
    post = Post()
    return render(request,'create.html',{'post':post})

  try:
      post.image = request.FILES['image']
  except:
      post.image = None



