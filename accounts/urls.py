from rest_framework import routers

from accounts.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'user/account', AccountViewSet, basename="user_account")
urlpatterns = router.urls
