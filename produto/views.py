from asyncio import Event
import json
from django.shortcuts import redirect, render
from .models import produto
from rest_framework import viewsets
from .serializers import ProdutoSerializer
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from .models import Price
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import produto, Price
from .serializers import ProdutoSerializer
import stripe
import json
from django.conf import settings
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]
stripe.api_key = settings.STRIPE_SECRET_KEY

def handle_checkout_completed_event(event):
    session = event['data']['object']
    customer_email = session["customer_details"]["email"]
    payment_intent = session["payment_intent"]
    line_items = stripe.checkout.Session.list_line_items(session["id"])
    stripe_price_id = line_items["data"][0]["price"]["id"]
    price = Price.objects.get(stripe_price_id=stripe_price_id)
    product = price.product
    send_mail(
        subject="Here is your product",
        message=f"Thanks for your purchase. The URL is: {product.url}",
        recipient_list=[customer_email],
        from_email="your@email.com"
    )

def handle_payment_intent_succeeded_event(event):
    intent = event['data']['object']
    stripe_customer_id = intent["customer"]
    stripe_customer = stripe.Customer.retrieve(stripe_customer_id)
    customer_email = stripe_customer['email']
    price_id = intent["metadata"]["price_id"]
    price = Price.objects.get(id=price_id)
    product = price.product
    send_mail(
        subject="Here is your product",
        message=f"Thanks for your purchase. The URL is {product.url}",
        recipient_list=[customer_email],
        from_email="your@email.com"
    )

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)  # Invalid payload
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)  # Invalid signature

    if event['type'] == 'checkout.session.completed':
        handle_checkout_completed_event(event)
        return HttpResponse(status=200)
    elif event["type"] == "payment_intent.succeeded":
        handle_payment_intent_succeeded_event(event)

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = ProdutoSerializer

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "https://yourdomain.com" if not settings.DEBUG else "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)

class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            req_json = json.loads(request.body)
            customer = stripe.Customer.create(email=req_json['email'])
            price = Price.objects.get(id=self.kwargs["pk"])
            intent = stripe.PaymentIntent.create(
                amount=price.price,
                currency='usd',
                customer=customer['id'],
                metadata={
                    "price_id": price.id
                }
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})

class CustomPaymentView(TemplateView):
    template_name = "custom_payment.html"
 
    def get_context_data(self, **kwargs):
        product = produto.objects.get(name="Test Product")
        prices = Price.objects.filter(product=product)
        context = super(CustomPaymentView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = produto.objects.all()
    serializer_class = ProdutoSerializer