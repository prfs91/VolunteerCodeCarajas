"""
URL configuration for sistema_carajas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from sistema_carajas import \
    views  # Isso assume que o views.py está dentro da pasta sistema_carajas, que é onde fica o urls.py principal.

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # URLs do Grappelli
    path('admin/', admin.site.urls), # URLs do Django Admin
    path('', views.home, name='home'),
    path('associados/', include('associados.urls')),  # <-- inclui as URLs do app
]
