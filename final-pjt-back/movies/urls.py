from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    
    path('movies/', views.movies),
    path('dataget/', views.dumpMovieDataGet),
    # # path('movies/<int:community_pk>/', views.community_detail),
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
