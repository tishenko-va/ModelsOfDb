from .views import sign_up_by_django, sign_up_by_html, main_page, cart_page, shop_page, news
from django.urls import path



urlpatterns = [
    path('', sign_up_by_django),
    path('by_html/', sign_up_by_html)
]




urlpatterns = [
    path('', main_page),
    path('shop/', shop_page),
    path('cart/', cart_page),
    path('by_html/', sign_up_by_html),
    path('by_dj/', sign_up_by_django),
    path('platform/news/', news)

]