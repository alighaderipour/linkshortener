from django.urls import path
from . import views

urlpatterns = [
    path('list', views.get_links),
    path('list/<slug:slug>/', views.track_click, name='track_click'),
    path('link/create/', views.create_link, name='create_link'),

]