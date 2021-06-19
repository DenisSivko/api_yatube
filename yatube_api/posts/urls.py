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
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
