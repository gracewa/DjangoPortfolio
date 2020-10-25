from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:pk>/", views.photo_detail, name="photo_detail"),
    path(r'search/', views.search_results, name='search_results'),
    path(r'location/<slug:search_term>/', views.search_locations, name='search_locations')

]