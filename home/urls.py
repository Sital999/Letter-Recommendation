from django.contrib import admin
from django.urls import path ,include
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('loginStudent', views.loginStudent, name='loginStudent'),
    path('loginTeacher', views.loginTeacher, name='loginTeacher'),
    path('logout', views.logoutUser, name='logout'),
    path('studentSuccess', views.studentSuccess, name='StudentSuccess'),
    path('makeLetter', views.make_letter, name='MakeLetter'),
    path('final', views.final, name='Final'),
    path('gallery', views.gallery, name='Gallery'),
]

