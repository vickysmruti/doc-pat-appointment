from django.shortcuts import render
from rest_framework.response import Response
from .models import Appointment,Doctor,Patient
from .serializers import AppointmentSerializer,PatientSerializer,DoctorSerializer
from rest_framework import viewsets
import datetime

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            con = Appointment.objects.filter(date= request.data['date'],doc=request.data['doc'],pat=request.data['pat'])
            dt = serializer.validated_data['date']
            now = datetime.date.today()
            if dt<now:
                return Response({'selected date invalid, choose a further date'})
            if con:
                return Response({'msg' : 'appointment already scheduled for the date and choose a further date'})
            serializer.save()
        return Response(serializer.errors)






