from django.conf.urls import url
from yfpool import views

urlpatterns = [
    url(r'^/$', views.list),
]
