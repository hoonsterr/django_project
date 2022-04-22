
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView
import user.views
from user.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user.views.index, name='index'),
    path('log/', include('user.urls')),
    path('', user.views.homepage),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
