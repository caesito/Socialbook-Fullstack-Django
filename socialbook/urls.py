from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
    path('search/', include('search.urls')),
    path('auth/',include('authentication.urls')),
    path('profile/', include('user_profile.urls'))
]
