from django.contrib import admin
from django.urls import path, include
from webapp import views
from webapp.views import UserViewSet
from webapp.views import csvDbViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UserData.as_view()),
    path('api/', include('webapp.urls')),
    path('db/', include('webapp.urls')),
]
