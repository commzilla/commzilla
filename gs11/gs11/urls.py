
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('c/', include('course.urls')),
    path('f/', include('fees.urls'))
]
