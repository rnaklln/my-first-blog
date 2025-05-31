from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post'),
    #path('', views.home, name='home'),
]
