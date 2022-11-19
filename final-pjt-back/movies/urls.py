from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views, tests

urlpatterns = [
    path('movies/', views.movies),
    path('dataget/', views.dumpMovieDataGet),
    path('datatest/', tests.datatest),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('genre/<int:genre_id>/', views.genre),
    path('movies/search/<str:text>/', views.movie_search),
    # path('smilar/<int:movie_id>/', views.smilar),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
