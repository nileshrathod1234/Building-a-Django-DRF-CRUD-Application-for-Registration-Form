from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Education, Skill, Registration

class RegistrationTests(APITestCase):
    def setUp(self):
        # Setup initial data
        self.education = Education.objects.create(qualification='Bachelor of Science')
        self.skill = Skill.objects.create(name='Python')

    def test_create_registration(self):
        """ 
        Ensure we can create a new registration object.
        """
        url = reverse('registration-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'higher_education': self.education.id,
            'skills': [self.skill.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Registration.objects.count(), 1)
        self.assertEqual(Registration.objects.get().first_name, 'John')


    

    # Test Case for Updating a Registration Entry.
        
    def test_update_registration(self):
        """
        Ensure we can update an existing registration object.
        """
        # First, create a registration object
        registration = Registration.objects.create(
            first_name='Jane', 
            last_name='Doe', 
            date_of_birth='1990-05-05', 
            higher_education=self.education,
        )
        registration.skills.add(self.skill)

        # URL for updating the registration
        url = reverse('registration-detail', kwargs={'pk': registration.id})

        # Data for update
        updated_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'date_of_birth': '1990-05-05',
            'higher_education': self.education.id,
            'skills': [self.skill.id]
        }

        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        registration.refresh_from_db()
        self.assertEqual(registration.last_name, 'Smith')

            




