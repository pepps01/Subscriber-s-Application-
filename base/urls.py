from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register("user", views.UserViewSet)
router.register("plan", views.PlanViewSet)
router.register("subscription", views.SubscriptionViewSet)
router.register("transaction", views.TransactionViewSet)
app_name = "base"
urlpatterns = [
    path("", include(router.urls)),
    path('user/documentation', views.user_doc),
    path('plan/documentation', views.plan_doc),
    path('subscribe/documentation', views.subscribe_doc),
    path('transact/documentation', views.transact_doc),
]
