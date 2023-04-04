from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("my_blog/", ListingBlogView.as_view(), name="my_blog"),
    path("home", home, name="home"),
    path("blog_detail/<int:id>/", BlogView.as_view(), name="blog_detail"),
    path("user_profile/<int:id>/", UserView.as_view(), name="user_profile"),
    path("delete_blog/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),
    path("search/", SearchView.as_view(), name="search_view"),

]