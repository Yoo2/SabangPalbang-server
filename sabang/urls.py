from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^room/$', views.room, name="room"),
    url(r'^user/$', views.user, name="user"),
    url(r'^board_write/$', views.board_write, name="board_write"),
    url(r'^board/$', views.board, name="board"),
    url(r'^board/(?P<board_id>\d+)/detail/$', views.board_detail, name="board_detail"),
    url(r'^comment/$', views.comment, name="comment"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^delete_room/$', views.delete_room, name="delete_room"),
    url(r'^board/(?P<board_id>\d+)/delete/$', views.delete_board, name="delete_board"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
