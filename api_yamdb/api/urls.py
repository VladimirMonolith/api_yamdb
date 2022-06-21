from django.urls import include, path
from rest_framework import routers

from api_yamdb.settings import API_VERSION

from .views import (
    CategoryViewSet, CommentViewSet, GenreViewSet,
    ReviewViewSet, TitleViewSet, UserCreateViewSet,
    UserReceiveTokenViewSet, UserViewSet
)

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

app_name = 'api'


urlpatterns = [
    path(
        f'{API_VERSION}/auth/signup/',
        UserCreateViewSet.as_view({'post': 'create'}),
        name='signup'
    ),
    path(
        f'{API_VERSION}/auth/token/',
        UserReceiveTokenViewSet.as_view({'post': 'create'}),
        name='token'
    ),
    path(f'{API_VERSION}/', include(router.urls)),
]
