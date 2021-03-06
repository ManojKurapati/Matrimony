"""matripro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from matriapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('admin/', admin.site.urls),
     path('',views.index,name='index'),
     path('myprofile/<slug:slug>/',views.myprofile,name='myprofile'),
     path('myhome/',views.myhome,name='myhome'),
     path('selfprofile/<slug:slug>/',views.selfprofile,name='selfprofile'), 
     path('photos/',views.photos,name='photos'), 
     path('profiles/',views.profiles,name='profiles'), 
     path('search/',views.search,name='search'), 
     path('step1/',views.step1,name='step1'), 
     path('step2/<uuid:matri_uuid>/',views.step2,name='step2'), 
     path('step3/<uuid:matri_uuid>/',views.step3,name='step3'),      
     path('step4/<uuid:matri_uuid>/',views.step4,name='step4'),
     path('edit/<uuid:matri_uuid>/', views.matridata_edit, name='matriedit'),
     path('register/',views.register,name='register'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name='logout'),
     path('deleted/<int:id>/',views.delete_photo,name='deletephoto')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
