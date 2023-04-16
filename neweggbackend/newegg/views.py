from django.shortcuts import render, redirect
from .serializers import ProductSerializer, UserSerializer, ShoppingCartSerializer
from django.views.generic import View
from .models import  Product, ShoppingCart, User
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(f'username: {username}, password: {password}')
        user = authenticate(username=username, password=password)
        print(f'user: {user}')
        # if user is not None:
            # request.session['user_id'] = user.id
        return Response({'status': 'success'})
        # else:
        #     return Response({'status': 'failure'})
        

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        return HttpResponse(f'User: {user.name}')


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
class CartRemove(View):
    def delete(self, request, product_id):
        ShoppingCart.objects.filter(id=product_id).delete()
        return redirect('cart_detail')


class CartAdd(APIView):
    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            cart_item = ShoppingCart.objects.create(
                product=product,
                price=product.product_price)
            serializer = ShoppingCartSerializer(
                cart_item, 
                context={'request': request}
            )
            return JsonResponse(serializer.data, status=201)
        except Product.DoesNotExist:
            return JsonResponse({'status': 'error'})

class CartDelete(APIView):
    

    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            cart_item = ShoppingCart.objects.get(product=product)
            cart_item.delete()
            return JsonResponse({'status': 'success'})
        except (Product.DoesNotExist, ShoppingCart.DoesNotExist):
            return JsonResponse({'status': 'error'})
# bypassing csrf token
# cart_add = csrf_exempt(CartAdd.as_view())
# time_tracker_detail = csrf_exempt(TimeTrackerDetail.as_view())

class OrderDetailsView(View):
    def get(self, request, customer_id):
        
        cart = ShoppingCart.objects.filter(customer_id=customer_id)
        product_ids = [item.product.id for item in cart]
        price_total = sum([item.price for item in cart])
        data = {
            'product_ids': product_ids,
            'price_total': price_total,
        }
        return JsonResponse(data)


class CartUpdate(generics.UpdateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

    def put(self, request, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.quantity = request.data.get('quantity')
        cart_item.save()
        return self.update(request, *args, **kwargs)