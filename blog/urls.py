from django.urls import path
from . import views

urlpatterns = [
    path('', views.zapros_new, name='zapros_new'),
    path('worker_list/', views.worker_list, name='worker_list'),
    path('worker_new/', views.worker_new, name='worker_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('level_list/', views.level_list, name='level_list'),
    path('level/<int:pk>/', views.level_detail, name='level_detail'),
    path('user', views.user, name='user'),
    path('zapros_list', views.zapros_list, name='zapros_list'),
    path('zapros/new/', views.zapros_new, name='zapros_new'),
    path('zapros/detail/<int:pk>', views.zapros_detail, name='zapros_detail'),
    path('zapros/awaits/<int:pk>', views.zapros_awaits, name='zapros_awaits'),
    path('zapros/delete/<int:pk>/<str:token>', views.zapros_delete, name='zapros_delete'),
    path('items_list', views.items_list, name='items_list'),
    path('item_new/', views.item_new, name='item_new'),
    path('item_detail/<int:pk>', views.item_detail, name='item_detail'),
    path('toner_list', views.toner_list, name='toner_list'),
    path('toner/edit/<int:pk>', views.toner_edit, name='toner_edit'),
    path('history_list', views.history_list, name='history_list'),
]