from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('drafts', views.draft_list, name='draft_list'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:pk>/publish', views.publish_draft, name='publish_draft'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment', views.post_comment, name='post_comment'),
    path('comment/<int:pk>/approve', views.post_comment_approve, name='post_comment_approve'),
    path('comment/<int:pk>/delete', views.post_comment_delete, name='post_comment_delete')
]