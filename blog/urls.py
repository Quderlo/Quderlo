from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('table/', views.table_list, name='table_list'),
    path('table/submit/', views.submit, name='submit'),
    path('table/n_m/', views.table_list_n_m, name='table_n_m'),
    path('table/n_m/submit', views.submit_n_m, name='submit_n_m')
]
