
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Tasks.views import home

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()


