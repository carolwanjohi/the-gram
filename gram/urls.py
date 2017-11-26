from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url( r'^$', views.timeline, name="timeline"),
    url( r'^profile/(\d+)', views.profile, name="profile"),
    url( r'^create/post', views.new_post, name="new-post"),
    url( r'^explore/(\d+)', views.explore, name="explore"),
    url( r'^follow/(\d+)', views.follow, name="follow"),
    url( r'^create/comment(\d+)', views.comment, name="comment" )
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

