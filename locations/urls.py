from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:pk>/', views.edit_location, name='edit_location'),
    path('delete/<int:pk>/', views.delete_location, name='delete_location'),
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),

]