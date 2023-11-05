from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
#
router.register('Mobile',MobileView,basename='Mobile')
router.register('Category',CategoryView,basename='Category')
router.register('Products',ProductsView,basename='Products')
router.register('ProductList',ProductListView,basename='ProductList')
router.register('Cart',CartView,basename='Cart')

urlpatterns = [
    # path('',MobileView.as_view()),
    path('',include(router.urls))
]