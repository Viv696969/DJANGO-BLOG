from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import Blogform,Profileform
from django.urls import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import generic,View

# Create your views here.

# def home(request):
#     return render(request,'home.html',{'name':'vivek'})

def like(request,pk):
    blog=get_object_or_404(Blog,id=pk)

    if blog.likes.filter(id=request.user.id).exists(): #if the user has like he will exist in the relationship table but when the user clicks again and if he exists he will removed for the dislike button
        blog.likes.remove(request.user) # remove the user 
        liked=False
    else:
        blog.likes.add(request.user)
        liked=True
    return redirect('article',pk)

class Home(View):
    # model=Blog
    # template_name='home.html'
    # ordering=['-blog_crated']
    def get(self,request):
        
        blog=Blog.objects.all().order_by('-id')
        cats=Category.objects.all()
        context={'blog':blog,'cats':cats}
        return render(request,'home.html',context)


    
    

class Article(View):
    # model=Blog
    # template_name='article.html'
    def get(self,request,pk):
        blog=Blog.objects.get(id=pk)
        b=Blog.objects.get(id=pk)
        liked=False
        if b.likes.filter(id=request.user.id).exists():#if that user exists in the manyto many relatonship with  the likes of the blog 
            liked=True
        likes=b.totallikes()
        context={'blog':blog,'likes':likes,'liked':liked}
        return render(request,'article.html',context)


class Create(CreateView):
    # model=Blog
    # form_class=Blogform
    # template_name='create.html'
    def get(self,request):
        form=Blogform()
        context={'form':form}
        return render(request,'create.html',context)

    def post(self,request):
        form=Blogform(request.POST,request.FILES)
        f=form.save(commit=False)
        f.author=request.user
        f.save()
        return redirect('home')
   
    

class Update(UpdateView):
    model=Blog
    template_name='update.html'
    fields=['title','body']


class Delete(DeleteView):
    model=Blog
    
    success_url=reverse_lazy('home')

class Register(generic.CreateView):
    # model=User
    form_class=UserCreationForm
    template_name='registration/register.html'
    
    success_url=reverse_lazy('login')



def category(request,cat):
    blogs=Blog.objects.filter(category=cat)
    return render(request, 'category.html',{'blogs':blogs})



#profiile

class CreateProfile(View):
    def get(self,request):
        form=Profileform()
        context={'form':form}
        return render(request,'profile.html',context)

    def post(self,request):
        form=Profileform(request.POST,request.FILES)
        f=form.save(commit=False)
        f.user=request.user
        f.save()
        return redirect('profile')

class Yourprofile(View):


    def get(self,request):
        blogs=Blog.objects.filter(author=request.user)
        if Profile.objects.filter(user=request.user).exists():
            obj=Profile.objects.get(user=request.user)
            exist=True
        else:
            exist=False
            obj=None
        # obj=Profile.objects.get(user=request.user)
        context={'obj':obj,'exist':exist,'blogs':blogs}
        return render(request,'yourprofile.html',context)


class Editprofile(View):
    
    def get(self,request):
        info=Profile.objects.filter(user=request.user).first()
        prof=Profileform(instance=info)
        context={'form':prof}
        return render(request,'updateprofile.html',context)


    def post(self,request):
        info=Profile.objects.filter(user=request.user).first()
        form=Profileform(request.POST,request.FILES,instance=info)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            context={'form':form,'error':'You misssed out something to fill'}
            return render(request,'updateprofile.html',context)



class Userprofile(View):
    def get(self,request,pk):
        prof=Profile.objects.filter(id=pk).first()
    
        context={'p':prof}
        return render(request,'userprofile.html',context)

