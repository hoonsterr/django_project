
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'login'
urlpatterns = [
    path('join/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('dbconn/', views.dbconn),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)