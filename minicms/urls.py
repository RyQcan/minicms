from django.conf.urls import url, include
from django.contrib import admin, auth
from news import views as news_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', news_views.index),
    url(r'^news/', include('news.urls', namespace='news')),
    # url('^', include('auth.urls', namespace='users')),
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
