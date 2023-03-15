from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    #path('tools', views.tools, name='tools'),
    path('',views.tools, name='tools'),
    path('translator',views.translator, name='translator'),
    path('translated', views.translated, name='translated'),
     path('analyze', views.analyze, name='analyze'),
     path('counter ', views.counter, name='counter'),
]

