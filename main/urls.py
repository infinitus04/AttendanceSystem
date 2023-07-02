from django.urls import path
from . import views
urlpatterns = [
    path('class/', views.classes, name = 'classes'),
    path('login/', views.loginfun, name = 'login'),
    path('class/<int:classid>', views.classDetails, name = 'classDetail'),
    path('atten/', views.getatten, name = 'atten'),
]
