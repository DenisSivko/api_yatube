from django.urls import include, path
from posts.views import CommentViewSet, PostViewSet
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, 'post')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, 'comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
