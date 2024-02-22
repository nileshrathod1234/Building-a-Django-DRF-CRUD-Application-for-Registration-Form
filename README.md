# Building-a-Django-DRF-CRUD-Application-for-Registration-Form
This project is a Django REST Framework (DRF) application for managing a registration form. It allows for CRUD operations on registration entries, including fields such as first name, last name, middle name, date of birth, higher education, and skills. 
# Features
* CRUD operations for registration entries
* Search functionality by name and date of birth
* Pagination for listing entries
* Admin interface for managing education and skill data
# Getting Started
* Python 3.6 or higher
* Django 3.0 or higher
* Django REST Framework
# Installation
1. Clone the repository:
   git clone [URL to your repository]
cd [repository name]
2. Install the required packages:
   pip install -r requirements.txt
3. Migrate the database::
4. 
   python manage.py makemigrations
   python manage.py migrate
5. Create a superuser (for accessing the admin panel):
   python manage.py createsuperuser
6. Run the server:
   python manage.py runserver
# API Endpoints
  ## Registration CRUD:
  * Creating a Registration Entry:
   1. Make a POST request to the registration endpoint (http://127.0.0.1:8000/api/registrations/).
   2. Include the necessary data in the request body (first name, last name, etc.).
  *  Retrieving Registration Entries:
     1. Make a GET request to the same endpoint to retrieve all registrations.
  *  Updating a Registration Entry:
     1. Send a PUT or PATCH request to http://127.0.0.1:8000/api/registrations/{id}/, where {id} is the ID of the registration you want to update.
  *  Deleting a Registration Entry:
     1. Send a DELETE request to http://127.0.0.1:8000/api/registrations/{id}/.
  ## Search and Pagination
  *  searching
     1. make a GET request to http://127.0.0.1:8000/api/registrations/?search={query}, where {query} is the name or date of birth you want to search for.
  *  pagination
  *  1. the API will automatically divide the results into pages. You can navigate through them by adding a page parameter in your GET request, like http://127.0.0.1:8000/api/registrations/?page=2.
     

    
    





