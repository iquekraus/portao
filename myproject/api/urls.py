from django.conf.urls import url
from .views import CommentListView
from .comment import CommentView

from .users import UserListView
from .user import UserView

app_name = 'main_app'

urlpatterns = [
    url(r'^comments/?$', CommentListView.as_view(), name='comments'),
    url(r'^comment/(?P<pk>[0-9]+)/?$', CommentView.as_view(), name='comment'),

    url(r'^users/?$', UserListView.as_view(), name='users'),
    url(r'^user/(?P<pk>[0-9]+)/?$', UserView.as_view(), name='user'),
]
