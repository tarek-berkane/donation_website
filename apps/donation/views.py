from chargily_epay_django.views import (
    CreatePaymentView,
    PaymentConfirmationView,
    PaymentObjectDoneView,
    FakePaymentView,
)

from apps.donation.forms import PaymentForm
from apps.donation.models import Payment


class Home(CreatePaymentView):
    template_name: str = "donation/home.html"
    form_class = PaymentForm


class PaymentConfirmation(PaymentConfirmationView):
    model = Payment


class PaymentStatus(PaymentObjectDoneView):
    template_name: str = "donation/donation_status.html"
    model = Payment


class FakePayment(FakePaymentView):
    model = Payment
