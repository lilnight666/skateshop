"""
URL configuration for lampioaoskt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework import viewsets
from produto.views import stripe_webhook
from produto.views import ProdutoViewSet
from usuarios.views import UserViewSet
from produto.views import StripeIntentView,CustomPaymentView
from produto.views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
)
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from produto.views import schema_view
router = routers.DefaultRouter()
router.register(r'produto', ProdutoViewSet)
router.register(r'USer', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("api-auth/",include("rest_framework.urls")),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('custom-payment/', CustomPaymentView.as_view(), name='custom-payment'),
    path(r'^$', schema_view),
]
