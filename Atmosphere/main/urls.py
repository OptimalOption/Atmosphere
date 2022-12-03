from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('about-the-company/', views.about, name='about'),
    path('directorate/', views.directorate, name='directorate'),
    path('news/', views.news, name='news'),
    path('licenses-and-certificates/', views.licenses, name='licenses'),
    path('training/', views.training, name='training'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('atmospheric-air-protection/', views.air, name='air'),
    path('environmental-protection-and-environmental-management/', views.environment, name='environment'),
    path('automatic-continuous-monitoring-of-industrial-emissions/', views.control, name='control'),
]
