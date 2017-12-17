from django.conf.urls import url, include
from news import views as news_views



urlpatterns = [
    url(r'^$', news_views.index, name='index'),
    url(r'about/$', news_views.about, name='about'),
    url(r'^auth/$', news_views.auth, name='auth'),
    url(r'^logout/$', news_views.logout_view, name='logout'),
    url(r'^upload/$', news_views.upload, name='upload'),
    url(r'^user_page/(?P<user_key>[^/]+)/$', news_views.user_page, name='user_page'),
    url(r'^column/(?P<column_slug>[^/]+)/$', news_views.column_detail, name='column'),
    url(r'^article/(?P<column_slug>[^/]+)/(?P<pk>\d+)/$', news_views.article_detail, name='article'),
    url(r'^edit/(?P<pk>\d+)/$', news_views.edit_page, name='edit_page'),
    url(r'^edit/action/$', news_views.edit_action, name='edit_action'),
]