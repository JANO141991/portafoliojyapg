from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.renderPosts, name='posts'),
    path("<int:post_id>", views.post_detail, name="post_detail"),
]