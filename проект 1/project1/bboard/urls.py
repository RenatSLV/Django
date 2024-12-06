from bboard.views import *
from django.urls import path
urlpatterns = [
    path('index/', index, name='index'),
    path('about_me/', about_me, name='about_me'),
    path('html/', index_html, name='index_html'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('crypto/<slug:slug>', get_by_slug, name='get_by_slug'),
    path('comment/<int:id>', get_comment_by_id, name='get_comment_by_id'),
    path('commentD/<int:id>', delete_comment_by_id, name='delete_comment_by_id'),

]