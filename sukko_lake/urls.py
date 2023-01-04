from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from sukko_lake import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'create_apps/',
        views.CreateApplicationView.as_view(),
        name='create_apps',
    ),
    path('', views.MainPageView.as_view(), name='main')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
