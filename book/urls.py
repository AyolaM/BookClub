
from django.contrib import admin
from django.urls import path, include
from poll import views
from search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('search/', views.search_book, name = 'search_book'),
    path('', include('search.url'))
]
