# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("admin", admin.site.urls),
    path('', views.index, name='home'),
    path('registrar-evento/', views.registrar_evento, name='registrar_evento'),
    path('registrar-medicamento/', views.registrar_medicamento, name='registrar_medicamento'),
    path('quantidade-medicamentos/', views.visualizar_medicamentos, name='quantidade_medicamentos')
    # re_path(r'^.*\.*', views.pages, name='pages'),
]
