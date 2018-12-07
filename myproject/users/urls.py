from django.conf.urls import url

from .users import UserListView
from .user import UserView

app_name = 'main_app'

urlpatterns = [
    url(r'^users/?$', UserListView.as_view(), name='users'),
    url(r'^user/(?P<pk>[0-9]+)/?$', UserView.as_view(), name='user'),
]