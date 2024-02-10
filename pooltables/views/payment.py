import requests
from django.conf import settings
from django.shortcuts import render
from django.views import View

def initiate_mpesa_payment(request):
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # Use sandbox URL for testing

    headers = {
        "Authorization": f"Bearer {settings.DARAJA_API_KEY}"
    }

    payload = {
        # ... (same payload as before)
    }

    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        checkout_request_id = response.json().get("CheckoutRequestID")
        payment_url = f"https://sandbox.safaricom.co.ke/mpesa/stkpush?phone={CUSTOMER_PHONE_NUMBER}&passkey={PASSKEY}&shortcode={YOUR_SHORTCODE}&lipa_na_mpesa_online_passkey={YOUR_LNM_PASSKEY}&callback_url={YOUR_CALLBACK_URL}&transaction_type=CustomerPayBillOnline&amount={AMOUNT_TO_PAY}&partyb={YOUR_SHORTCODE}&partyb={CUSTOMER_PHONE_NUMBER}&partyb={YOUR_CALLBACK_URL}&partyb={UNIQUE_ORDER_ID}"

        return render(request, 'mpesa_redirection.html', {'payment_url': payment_url})
    else:
        error_message = response.json().get("errorMessage")
        return render(request, 'error.html', {'error_message': error_message})
