from django.urls import path
from . import views

app_name = 'webapp'
urlpatterns = [
   # path('', views.index),
   path('', views.PostList.as_view(), name='index'),
   path('createform/', views.createform, name='createform'),
   path('logout/', views.logout, name='logout'),
   path('signin/', views.signin, name='login'),
   path('delete/<int:pk>/', views.data_delete, name='delete'),
]