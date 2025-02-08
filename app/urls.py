from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('genres.urls')),
    path('api/vi/', include('actors.urls')),
    path('api/v1/', include('movies.views')),
    path('api/v1/', include('reviews.views')),
]
