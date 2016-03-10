
from django.conf.urls import url, include
from django.contrib import admin
import social.apps.django_app.urls
import paypal.standard.ipn.urls

from einc import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('einc.urls')),
    url(r'^accounts/logout/$', views.account_logout, name='logout'),
    url(r'^accounts/login/$', views.home, name='login'),
    url(r'^accounts/profile/$', views.account_profile, name='profile'),

    url(r'^payment/cart/$', views.paypal_pay, name='cart'),
    url(r'^payment/success/$', views.paypal_success, name='success'),
    
    url('', include(social.apps.django_app.urls, namespace='social')),
    url(r'^paypal/', include(paypal.standard.ipn.urls)),
]
