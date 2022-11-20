from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.community_list),
    path('community/<int:community_pk>/', views.community_detail),
    # path('community/tag/<int:tag_pk>/', views.tag_research_pk),
    path('community/tag/<str:tag_str>/', views.tag_research_str),
    # path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    # path('articles/<int:article_pk>/comments/', views.comment_create),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
