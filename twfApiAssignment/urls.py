from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from twfApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('twfApi.urls')),
]
#binds functions to methods as_view()
#get with get , post with post method etc
urlpatterns=format_suffix_patterns(urlpatterns)