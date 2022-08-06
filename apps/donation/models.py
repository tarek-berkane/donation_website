from django.db import models
from django.urls import reverse

# Create your models here.
from chargily_epay_django.models import AnonymPayment, FakePaymentMixin


class Payment(FakePaymentMixin, AnonymPayment):
    webhook_url = "donation-confirmation"  # reverse url
    back_url = "donation-status"  # reverse url
    fake_payment_url = "fake-payment"  # reverse url

    def generate_back_url(self):
        confirmaion_url = str(
            reverse(self.back_url, kwargs={"pk": self.invoice_number})
        )
        return confirmaion_url
