from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




router=DefaultRouter()

router.register('products',views.ProductViewSet)
router.register('customer',views.CustomerViewSet)
router.register('order',views.OrderViewSet)
router.register('category',views.CategoryViewSet)

urlpatterns=[
    path('',views.api_root),
    path('',include(router.urls)),
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('register/',views.Register),
]

