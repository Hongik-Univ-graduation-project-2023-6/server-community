from rest_framework import routers
from .views import PostViewSet, CommentViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'image', ImageViewSet)

urlpatterns = router.urls
