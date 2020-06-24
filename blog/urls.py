from django.urls import path
from . import views

urlpatterns = [
    path('', views.zapros_new, name='zapros_new'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('level_list/', views.level_list, name='level_list'),
    path('level/<int:pk>/', views.level_detail, name='level_detail'),
    path('user', views.user, name='user'),
    path('zapros_list', views.zapros_list, name='zapros_list'),
    path('zapros/new/', views.zapros_new, name='zapros_new'),
    path('zapros/detail/<int:pk>', views.zapros_detail, name='zapros_detail'),
    path('zapros/awaits/<int:pk>', views.zapros_awaits, name='zapros_awaits'),
    path('zapros/delete/<int:pk>/<str:token>', views.zapros_delete, name='zapros_delete'),
]