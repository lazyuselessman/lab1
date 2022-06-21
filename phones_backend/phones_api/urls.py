from django.urls import include, path
from rest_framework import routers
from phones_api.views import UserViewSet, PhoneViewSet, NumberViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = routers.DefaultRouter()
router.register(r'phone', PhoneViewSet)

router.register(r'number', NumberViewSet)

router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]