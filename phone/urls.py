from django.urls import path
from . import views

urlpatterns = [
    path('', views.mobile_list, name='mobile_list'),
    path('new/', views.mobile_create, name='mobile_create'),
    path('brands/', views.brand_list, name='brand_list'),
    path('a/', views.mobile_list2, name='brand_filter'),
    path('search/', views.mobile_search, name='mobile_search'), 
    path('brand_filter/', views.phones_with_matching_nationality, name='brand_filterr'),

]
