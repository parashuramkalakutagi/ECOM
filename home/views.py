from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from rest_framework import viewsets
from . data_extraction import Mobiles_data_exctraction,Laptop_data_extraction
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,GenericAPIView
from .serializers import*
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination,CursorPagination
from rest_framework import pagination
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import mixins
import re

from .paymentgateway import *
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def validate_args(data, args):
    for key in args:
        if key not in data.keys():
            return Response({"message": f"Invalid Arguments, required {key}", "code": 400}, status=HTTP_400_BAD_REQUEST)

    return False

def validate_email_address(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False




class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class Pagination(CustomPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 6


class MobileView(viewsets.ReadOnlyModelViewSet):
    Mobiles_data_exctraction()
    queryset = Mobiles.objects.all()
    serializer_class = MobileSerializer
    filter_backends = [filters.SearchFilter ,filters.OrderingFilter]
    search_fields = ['^Product_Name','^Product_Price']
    ordering_fields = ['Product_Price']
    pagination_class = Pagination


class CategoryView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                response_data = {
                    'status_code': 201,
                    'data': serializer.data,
                }
                return Response(response_data,status=HTTP_201_CREATED)

        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_400_BAD_REQUEST,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_400_BAD_REQUEST)


class ProductsView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            user = request.user
            user = Profile.objects.get(email=user)
            validate = validate_args(data,['product_image','title','price','catagory','discount_price','description','currency'])
            if validate:
                return validate
            try:
                if user.is_admin:
                    obj = item.objects.create(
                        product_image=data['product_image'],
                        user=user,
                        title=data['title'],
                        price=data['price'],
                        catagory=Catagory.objects.get(catagory_name=data['catagory']),
                        discount_price=data['discount_price'],
                        description=data['description'],
                        currency='INR'
                    )
                    obj.save()
                    return Response({'message': 'Product created', 'code': 201}, status=HTTP_201_CREATED)
                else:
                    return Response({'message':'Only admin can Access this page ','code':400},status=HTTP_400_BAD_REQUEST)

            except Exception as e:
                print(e)
                response_data = {
                    'status_code': HTTP_400_BAD_REQUEST,
                    'error': str(e),
                    'message': 'Something went wrong.'
                }
                return Response(response_data, status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_400_BAD_REQUEST,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_400_BAD_REQUEST)
        
class ProductListView(viewsets.ReadOnlyModelViewSet):
    queryset = item.objects.all()
    serializer_class = ProductSerializer




class CartView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            validate = validate_args(data,['items','quntity'])
            if validate:
                return validate
            # obj = Cart.objects.get(user=request.user,items = data['items'],quntity = data['quntity'])

            objs = Cart.objects.create(
                    user = request.user,
                    items = item.objects.get(uuid = data['items']),
                    quntity=data['quntity'],
                )
            objs.save()
            return Response({'msg':'Cart Objects Created','Code':201},status=HTTP_201_CREATED)

        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_400_BAD_REQUEST,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data,status=HTTP_400_BAD_REQUEST)

    def patch(self,request,*args,**kwargs):
        try:
            data = request.data
            obj = Cart.objects.get(user = request.user,items=data['items'])
            if obj:
                obj.quntity = data['quntity']
                obj.save()
                return Response({'msg':'Cart Updated..','Code':200},status=HTTP_200_OK)
        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_400_BAD_REQUEST,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_400_BAD_REQUEST)

class OrderView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def create(self,request,*args,**kwargs):
        try:
            data = request.data
            user = request.user
            # validate = validate_args(data,['first_name','last_name','email','address','amount',])
            # if validate:
            #     return validate
            order_obj = order.objects.create(
                user=user,
                items=Cart.objects.get(uuid=data['items']),
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                address=data['address'],
                ordered='True',
                amount=data['amount'],
                currency='INR',
            )
            created_orderdata = RazorpayClient.create_order(self, int(data['amount']), data['currency'])
            order_obj.save()
            adress = Adress.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                order_confirmed='True',
                order_details=order.objects.get(uuid=order_obj.uuid)
            )
            adress.save()
            return Response({'data': created_orderdata, 'Code': 201}, status=HTTP_201_CREATED)
        except Exception as e:
            print(e)
            response_data = {
                'status_code': HTTP_400_BAD_REQUEST,
                'error': str(e),
                'message': 'Something went wrong.'
            }
            return Response(response_data, status=HTTP_400_BAD_REQUEST)

class Amount_transactionView(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        data = request.data
        user = request.user
        data['user'] = user
        serializer = AmountTransactionSerializer(data=data)
        if serializer.is_valid():
            RazorpayClient.verify_payment(
                razorpay_order_id=serializer.validated_data.get('order_id'),
                razorpay_singnature=serializer.validated_data.get('signature'),
                razorpay_payment_id=serializer.validated_data.get('payment_id'),
            )
            serializer.save()
            return Response({'msg':'Transaction is Successfully ','code':201},status=HTTP_201_CREATED)
        return Response({'msg':'Invalid Transaction'},status=HTTP_400_BAD_REQUEST)













