from django.contrib import admin
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('patient',views.PatientViewset,basename='patient')
router.register('doctor',views.DoctorViewset,basename='doctor')
router.register('appointment',views.AppointmentViewset,basename='appointment')

urlpatterns = [
    path('',include(router.urls)),
]
