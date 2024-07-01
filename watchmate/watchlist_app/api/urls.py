from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-detail'),
    path('', include(router.urls)),
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    
    # V1
    # path('list/', views.movie_list, name='movie-list'),
    # path('<int:pk>/', views.movie_details, name='movie-details'),
    
    # V2
    # path('list/', views.MovieListAV.as_view(), name='movie-list'),
    # path('<int:pk>/', views.MovieDetailAV.as_view(), name='movie-details'),
    
    # V3
    # path('review/', views.ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    # path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
]