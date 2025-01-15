"""
URL configuration for fluxify_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [ 
    path('home', views.home,name='home_page'),
    path('settings', views.settings,name='settings_page'),
    path('chat', views.chat,name='chat_page'),
    path('profile', views.profile,name='profile_page'),
    path('', views.login,name='login_page'),
    path('signup', views.signup,name='signup_page'),
    path('logout', views.user_logout,name='logout'),
    


    
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
