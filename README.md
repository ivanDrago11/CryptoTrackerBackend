Crypto Tracker Backend
This is the backend part of the Crypto Tracker application built with Django and Django REST Framework. The project uses MySQL as the database and JWT for authentication.

Features
Custom user model
JWT authentication
CRUD operations for managing users, cryptocurrencies, and crypto lists
Secure and scalable API design
Technologies
Django
Django REST Framework
MySQL
djangorestframework-simplejwt
Getting Started
Prerequisites
Python (version X.X.X)
MySQL (version X.X.X)
pip
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/crypto-tracker-backend.git
cd crypto-tracker-backend
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Setting Up the Database
Create a MySQL database:

sql
Copy code
CREATE DATABASE CryptoTrackerDB;
Update the DATABASES setting in backend/settings.py with your MySQL credentials:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CryptoTrackerDB',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Running Migrations
Run database migrations:
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Running the Server
Start the development server:

bash
Copy code
python manage.py runserver
Open your browser and navigate to http://localhost:8000.

Environment Variables
Create a .env file in the root directory and add any required environment variables:

plaintext
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
Project Structure
tracker/models.py: Django models
tracker/serializers.py: Django REST Framework serializers
tracker/views.py: Django views
tracker/urls.py: URL configurations
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.
