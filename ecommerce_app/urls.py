from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList, UserDetail, ProductList, ProductDetail, CartList, CartDetail

urlpatterns = [
	url('users/$', UserList.as_view()),
	url('users/(?P<pk>[0-9]+)/$', UserDetail.as_view())
	url('products/$', ProductList.as_view()),
	url('products/(?P<pk>[0-9]+)/$', ProductDetail.as_view())
	url('carts/$', CartList.as_view()),
	url('carts/(?P<pk>[0-9]+)/$', CartDetail.as_view())
]