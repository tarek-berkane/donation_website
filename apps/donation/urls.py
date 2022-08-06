from django.urls import path
from apps.donation.views import *


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path(
        "donation-confirmation/",
        PaymentConfirmation.as_view(),
        name="donation-confirmation",
    ),
    path(
        "donation-status/<int:pk>/",
        PaymentStatus.as_view(),
        name="donation-status",
    ),
    path(
        "fake-payment/<int:invoice_number>/",
        FakePayment.as_view(),
        name="fake-payment",
    ),
]
