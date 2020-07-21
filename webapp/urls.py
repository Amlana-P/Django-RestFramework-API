from rest_framework.routers import SimpleRouter
from webapp.views import UserViewSet
from webapp.views import csvDbViewSet

router = SimpleRouter()
router.register(r'csvDb', csvDbViewSet, basename='db')
router.register(r'users', UserViewSet, basename='api')
urlpatterns = router.urls