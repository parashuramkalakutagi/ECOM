import razorpay
from django.conf import settings
from rest_framework.serializers import ValidationError
from rest_framework import status

client = razorpay.Client(auth=(
    settings.RAZORPAY_KEY_ID,
    settings.RAZORPAY_SECREATE_ID
))


class RazorpayClient:
    def create_order(self,amount,currency):
        data = {
            "amount": amount*100,
            "currency" : "INR",
        }
        try:
            order_data = client.order.create(data = data)
            return order_data
        except Exception as e:
            raise ValidationError({
                "status_code ": status.HTTP_400_BAD_REQUEST,
                "error " : e
            })

    def verify_payment(self,razorpay_order_id,razorpay_payment_id,razorpay_singnature):
        try:
            return client.utility.verify_payment_singnature({
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_singnature': razorpay_singnature,
            })
        except Exception as e:
            raise ValidationError({
                "status_code ": status.HTTP_400_BAD_REQUEST,
                "error ": e
            })