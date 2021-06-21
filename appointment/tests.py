import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Doctor, Patient, Appointment


class DoctorTestCase(APITestCase):

    def setUp(self):
        self.doctor = Doctor.objects.create(name='sid', email='sid@gmail.com', specialization='ayurved')

    new = {'name': 'vishal', 'email': 'vishal@gmail.com', 'specialization': 'homeopathy'}

    """to create a new Doctor object."""

    def test_create_doctor(self):
        url = reverse('doctor-list')
        data = {'name': 'sid', 'specialization': 'ayurved', 'email': 'sid@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    """ to get Doctor object"""

    def test_get_doctor(self):
        url = reverse('doctor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """ to fully update Doctor object"""

    def test_put_doctor(self):
        url = reverse('doctor-detail', kwargs={'pk': self.doctor.pk})
        data = json.dumps(self.new, indent=4)
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """to partial update a Doctor object."""

    def test_update_doctor(self):
        url = reverse('doctor-detail', kwargs={'pk': self.doctor.pk})
        data = {'name': 'bunty', 'email': 'bunty@gmail.com'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """to delete a Doctor object."""

    def test_delete_doctor(self):
        url = reverse('doctor-detail', kwargs={'pk':self.doctor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class PatientTestCase(APITestCase):
    def setUp(self):
        self.patient = Patient.objects.create(name='siba', address='hinjili', phone=876543, email='siba@gmail.com', symptoms='viral')

    new = {'name': 'deepak','address': 'hinjili', 'phone':467899, 'email': 'deepak@gmail.com', 'symptoms': 'smallpox'}

    """to create a new Patient object."""

    def test_create_patient(self):
        url = reverse('patient-list')
        data = {'name': 'siba', 'address': 'hinjili', 'phone': 876543, 'email': 'siba@gmail.com', 'symptoms': 'viral'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    """ to get Patient object"""

    def test_get_patient(self):
        url = reverse('patient-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """ to fully update Patient object"""

    def test_put_patient(self):
        url = reverse('patient-detail', kwargs={'pk': self.patient.pk})
        data = json.dumps(self.new)
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """to partial update a patient"""

    def test_update_patient(self):
        url = reverse('patient-detail', kwargs={'pk': self.patient.pk})
        data = {'name': 'deepak','phone': 876543, 'email': 'deepak@gmail.com'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """to delete a Patient object."""

    def test_delete_patient(self):
        url = reverse('patient-detail', kwargs={'pk': self.patient.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AppointmentTestCase(APITestCase):

    def setUp(self):
        self.doctor = Doctor.objects.create(name='vishal', email='vishal@gmail.com', specialization='homeopathy')
        self.patient = Patient.objects.create(name='deepak', address='hinjili', phone=467899, email='deepak@gmail.com',                                      symptoms='smallpox')
        self.a = Appointment.objects.create(pat=self.patient, doc=self.doctor, date='2021-05-25', time='10:00:00')
        self.new = {'date': '2021-06-12', 'time': '12:00:00', 'doc': 5, 'pat': 7}

    """to create a new Appointment object. """

    def test_create_appointment(self):
        url = reverse('appointment-list')
        data = {'date': '2021-05-25', 'time': '10:00:00', 'doc': self.doctor.pk, 'pat': self.patient.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """to get appointment object """

    def test_get_appointment(self):
        url = reverse('appointment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """ to fully update Appointment object"""

    def test_put_appointment(self):
        url = reverse('appointment-detail', kwargs={'pk': self.a.pk})
        data = json.dumps(self.new)
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """to partial update appointment"""

    def test_update_appointment(self):
        url = reverse('doctor-detail', kwargs={'pk': self.a.pk})
        data = {'date': '2021-05-28'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """to delete a Appointment object."""

    def test_delete_appointment(self):
        url = reverse('appointment-detail', kwargs={'pk': self.a.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

