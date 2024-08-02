# Crypto Tracker Backend

This is the backend part of the Crypto Tracker application built with Django and Django REST Framework. The project uses MySQL as the database and JWT for authentication.

## Features

- Custom user model
- JWT authentication
- CRUD operations for managing users, cryptocurrencies, and crypto lists
- Secure and scalable API design

## Technologies

- Django
- Django REST Framework
- MySQL
- djangorestframework-simplejwt

## Getting Started

### Prerequisites

- Python (version X.X.X)
- MySQL (version X.X.X)
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crypto-tracker-backend.git
    cd crypto-tracker-backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Setting Up the Database

1. Create a MySQL database:
    ```sql
    CREATE DATABASE CryptoTrackerDB;
    ```

2. Update the `DATABASES` setting in `backend/settings.py` with your MySQL credentials:
    ```python
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
    ```

### Running Migrations

1. Run database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### Running the Server

1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and navigate to `http://localhost:8000`.

### Environment Variables

Create a `.env` file in the root directory and add any required environment variables:
```plaintext
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
