from django.urls import path
from .views import hello, HelloView
from .views import year_post, MothPost, post_detail
from .views import my_view, TempIf, view_for, index, about, author_posts, post_full

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>', MothPost.as_view(), name='moth_post'),
    path('posts/<int:year>/<int:moth>/<slug:slug>', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('tempif/', TempIf.as_view(), name='index2'),
    path('templ_for/', view_for, name="view_for"),
    path('index/', index, name="index"),
    path('about/', about, name="about"),
    path('author/<int:author_id>/', author_posts, name="author_posts"),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
