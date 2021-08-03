from django.urls import path, include
from .views import( 
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )
from .views import PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostViewSet, basename="posts")

urlpatterns = [
    path('', include(router.urls)),
    path('home/',PostListView.as_view(),name="blog-home"),
    path('user/<str:username>/',UserPostListView.as_view(), name='user-posts'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
 
]