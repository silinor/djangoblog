"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views
from blog_post.views import PostAddView, PostListView, PostDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', PostListView.as_view(), name='front'),
    url(r'^blog/$', PostListView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='blog-detail'),
    url(r'^register/$', RegistrationView.as_view(), name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^blog/add/$', PostAddView.as_view(), name='blog-add'),
]

