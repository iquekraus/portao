from django.conf.urls import url
from .views import CommentListView
from .comment import CommentView

app_name = 'main_app'

urlpatterns = [
    url(r'^comments/?$', CommentListView.as_view(), name='comments'),
    url(r'^comment/(?P<pk>[0-9]+)/?$', CommentView.as_view(), name='comment'),
]
