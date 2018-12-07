from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include('comments.urls', namespace='comments')),
    url(r'^v1/', include('users.urls', namespace='users')),
]
