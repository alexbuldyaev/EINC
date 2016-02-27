from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^countosg/', views.post_count, name='post_count'),
    url(r'^countksk/', views.post_countksk, name='post_countksk'),
    url(r'^counthom/', views.post_counthom, name='post_counthom'),
    url(r'^signin/', views.post_signin, name='post_signin'),
    url(r'^bepay/', views.post_bepay, name='post_bepay'),
    url(r'^contact/', views.post_contact, name='post_contact'),

]
