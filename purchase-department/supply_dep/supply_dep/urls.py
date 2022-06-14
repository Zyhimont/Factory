"""supply_dep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from supply import router, api, viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('supply.router')),
    path('api/', include(router.urlpatterns)),
    path('index/', viewsets.index),

    path('materials_list/', viewsets.materials_list),
    path('create_material/', viewsets.create_material),
    path('update_material/', viewsets.update_material),
    path('delete_material/', viewsets.delete_material),

    path('feedstock_list/', viewsets.feedstock_list),
    path('create_feedstock/', viewsets.create_feedstock),
    path('update_feedstock/', viewsets.update_feedstock),
    path('delete_feedstock/', viewsets.delete_feedstock),

]
