"""social_registraton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from login.forms import LoginForm
from login.views import register, ProfileView, login
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', register, name='register'),
    url(r'^profile/', ProfileView.as_view(), name='profile'),
    # url(r'^home/$', home, name='home'),
    # url(r'^login/$', login, name='login'),
    # url(r'^accounts/social/signup/', 'mainapp.signup_views.signup_view', name = 'account_signup'),
    url(r'^login/$', login ,name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

