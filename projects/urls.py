from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^profile/(\d+)$', views.profile, name='profile'),
    url(r'^update_profile/(\d+)$', views.update_profile, name='update_profile'),
    url(r'^projects/(?P<pk>\d+)/$', views.project, name='project'),
    url(r'^upload/$', views.upload_project, name='upload'),
    url(r'^search_project/$', views.search_project, name='search_project'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
