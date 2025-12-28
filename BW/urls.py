# Import ur urls here

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from BW.views import HomeView, ShopView, AboutView, DescitptionView, OrderView, OrderEndView, CartView

urlpatterns = [
    path('', HomeView.as_view(), name='greetings_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    
    path('store/', ShopView.as_view(), name='main_store_page'),
    path('bike/<int:bikeid>', DescitptionView.as_view(), name='bike_page'),
    
    path('order/', OrderView.as_view(), name='order_page'),
    path('order_end/', OrderEndView.as_view(), name='order_end_page'),
    
    path('cart', CartView.as_view(), name='cart_page')

    # path('bike/update/<int:bikeid>', UpdateView.as_view(), name='bike_update_page'),
    # path('bike/delete/<int:bikeid>', DeleteView.as_view(), name='bike_delete_page'),
    
    # path('search/', SearchView.as_view(), name='search_page'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)