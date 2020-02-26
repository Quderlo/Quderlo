from django.urls import path
from . import views

# TODO: удалить страницы, которые не используются, в том числе про блоги из Django girls

urlpatterns = [
    path('table/', views.table_list, name='table_list'),
    path('table/submit/', views.submit, name='submit'),
    path('table/n_m/', views.table_list_n_m, name='table_n_m'),
    path('table/n_m/submit', views.submit_n_m, name='submit_n_m')
]
