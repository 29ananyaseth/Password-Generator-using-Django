Password Generator

A simple and customizable password generator built with Django. This web application allows users to generate secure passwords based on their preferences, such as length and character types (uppercase, lowercase, digits, and special characters).

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features

Customizable Password Length: Users can specify the length of the password (default is 12 characters).

Character Type Selection: Users can choose which types of characters to include in the password:

      Uppercase Letters (A-Z)

      Lowercase Letters (a-z)

      Digits (0-9)

      Special Characters (!@#$%^&*, etc.)

Secure Password Generation: Passwords are generated using Python's random and string modules.

User-Friendly Interface: Simple and intuitive web interface for generating passwords.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Screenshots


Home Page
![Screenshot 2025-01-31 172647](https://github.com/user-attachments/assets/616be390-05df-4c90-885f-827564d55e25)


Generated Password
![Screenshot 2025-01-31 172704](https://github.com/user-attachments/assets/f967bc20-8f1f-4e26-abb8-4cb93adce864)

-----------------------------------------------------------------------------------------

Installation


Follow these steps to set up the project locally:

Prerequisites:


Python 3.x & 
Django 4.x


Steps

1-Clone the Repository:

git clone https://github.com/your-username/password-generator.git
cd password-generator

2-Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3-Install Dependencies:

pip install -r requirements.txt

4-Run Migrations:

python manage.py migrate


5-Start the Development Server:

python manage.py runserver


6-Access the Application:

Open your browser and go to http://127.0.0.1:8000/.
---------------------------------------------------------------------------------------

Project Structure

password-generator/
├── FirstProject/                  # Django project folder
│   ├── __init__.py
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── passgenerator/                 # Django app folder
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py                   # Password generation logic
│   └── templates/                 # HTML templates
│       ├── passgenerator/
│           ├── home.html          # Home page template
│           └── password.html      # Password display template
├── manage.py                      # Django management script
├── db.sqlite3                     # SQLite database (development)
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation

-------------------------------------------------------------------------------------


Usage

1-Open the application in your browser.

2-On the home page, specify the desired password length and select the character types you want to include.

3-Click "Generate Password".

4-The generated password will be displayed on the next page.

------------------------------------------------------------------------

Acknowledgments


Built with Django.

Inspired by the need for simple and secure password generation tools.

--------------------------------------------------------------------------------------
