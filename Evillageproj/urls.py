"""
URL configuration for Evillageproj project.

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
from django.contrib import admin
from django.urls import path
from general import views
from AdminZone import views as ad
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('register/',views.register),

    path('photo/',views.photo),

    path('schemes/',views.schemes),

    path('links/',views.links),

    path('bhulekha/',views.bhulekha),

    path('manrega/',views.manrega),

    path('schloorships/',views.schloorships),

    path('login/',views.login),

    path('contact/',views.contact),
    path('dash/',ad.dashboard),
    path('feedbackmgmt/',ad.feedbackmgmt),
    path('responsemgmt/',ad.responsemgmt),
    path('enquirymgmt/',ad.enquirymgmt),
    path('feedbackmgmt/',ad.feedbackmgmt),
    path('dynamicupdations/',ad.dynamicupdations),
    path('registrationmgmt/',ad.registrationmgmt),
    path('settingsmgmt/',ad.settingsmgmt),
    path('chagepassword/',ad.changepassword),
    path('contactData/',views.contactData),
    path('loginData/',views.loginData),
    path('logoutData/',ad.logoutData),
    path('addscheme/',ad.addscheme),
    path('delData/<int:id>',ad.delData),
    path('changeData/',ad.chageData),
    path('forget/',views.forget),
    path('otp/',views.otp),
    path('newpass/',views.newpass),
    path('forgetData/',views.forgetData),
    path('otpData/',views.otpData),



]
