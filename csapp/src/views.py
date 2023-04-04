from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *
# https://towardsdatascience.com/top-12-ways-to-learn-aws-for-free-1113af329d06

# @login_required
def home(request):
  blogs_objs = Blog.objects.order_by('-created_at')
  return render(request, 'home.html', context = {"blogs": blogs_objs})


class UserView(View):
  def get(self, request, id):
    user_obj = User.objects.filter(id=id).first()
    if user_obj:
      context = {"user_obj": user_obj}
      return render(request, "user_profile.html", context=context)
    return HttpResponse("User not fount sorry for the inconvenience")


class LoginView(View):
  template_name = 'login.html'
  def get(self, request):
    return render(request, 'login.html')

  def post(self, request):
      try:
        user = User.objects.get(email= request.POST.get('email'))
        auth_user = authenticate(
            username= user.username,
            password= request.POST.get('password'),
        )
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
      except Exception as e:
        print(e)
        message = 'Login failed!'
        return render(request, self.template_name, context={'message': message})


class BlogView(View):
  def get(self, request, id):
    blog_obj = Blog.objects.filter(id=id).first()
    if blog_obj:
      comment_obj = Comment.objects.filter(blog=blog_obj.id, sub_comment_of__isnull=True)
      context = {'blog_obj':blog_obj, "comment_obj": comment_obj}
      return render(request, "blog_detail.html", context=context)
    return HttpResponse("Blog not found sorry for the inconvenience")


class BlogDeleteView(View):
  def get(self, request, pk):
    blog_obj = Blog.objects.filter(id=pk).first()
    if blog_obj:
      blog_obj.delete()
      return redirect('my_blog')
    return redirect('my_blog')


class SearchView(View):
  def get(self, request):
    text = request.GET.get('text')
    blogs_objs = Blog.objects.filter(title__icontains= text).order_by('-created_at')
    return render(request, 'home.html', context = {"blogs": blogs_objs})
    

class ListingBlogView(View):
  def get(self, request):
    # import pdb;pdb.set_trace()
    login_user = request.user
    blog_obj = Blog.objects.filter(author__id = login_user.id).order_by("-created_at")
    return render(request, 'my_blog.html', context = {"blog_obj": blog_obj})
