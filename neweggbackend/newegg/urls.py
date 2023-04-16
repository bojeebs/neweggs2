from django.urls import path
from . import views




urlpatterns = [
     
     path('api/user/create/', views.CreateUserView.as_view(), name='customer'),
     path('api/user/login/', views.LoginView.as_view(), name='login'),
     path('api/user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
     path('product/', views.ProductList.as_view(), name='products'),
     path('api/product/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
     path('api/cart/update/<int:pk>/', views.CartUpdate.as_view(), name='cart_update'),
     path('cart/remove/<int:product_id>/', views.CartRemove.as_view(), name='remove_cart'),
     path('cart/add/<int:product_id>/', views.CartAdd.as_view(), name='cart_add'),
     path('api/cart/delete/<int:product_id>/', views.CartDelete.as_view(), name='cart_delete'),
     path('order_details/<int:customer_id>/', views.OrderDetailsView.as_view(), name='order_details'),

]